
from .Util import log_error, suppress_stdout_stderr

class BackendDetect:
    def __init__(self):
        self.__torch = None
        self.__tensorrt = None
        self.__ncnn = None
        self.pytorch_device = None
        self.pytorch_version = None
        try:
            import torch
            import torchvision
            self.__torch = torch
            self.pytorch_device = self.__get_pytorch_device()
            self.pytorch_version = self.__torch.__version__
            try:
                with suppress_stdout_stderr():
                    import tensorrt
                    import torch_tensorrt
                self.__tensorrt = tensorrt
            except ImportError as e:
                pass
            except Exception as e:
                pass
        except ImportError as e:
            pass
        except Exception as e:
            pass
        try:
            from rife_ncnn_vulkan_python import Rife
            import ncnn

            try:
                from upscale_ncnn_py import UPSCALE
            except ImportError:
                pass
            self.__ncnn = ncnn
        except ImportError as e:
            pass
        except Exception as e:
            pass



    def __get_pytorch_device(self):
        ver = self.__torch.__version__.lower()
        if "rocm" in ver: return "rocm"
        if "cu" in ver:
            try:
                if self.__torch.cuda.is_available(): return "cuda"
                if self.__torch.xpu.is_available(): return "xpu"
                if self.__torch.backends.mps.is_available(): return "mps"
            except Exception:
                pass
            return "CPU"
        if self.__torch.xpu.is_available(): return "xpu"
        if self.__torch.backends.mps.is_available(): return "mps"
        try:
            if self.__torch.cuda.is_available(): return "cuda"
        except Exception:
            pass
        return "CPU"

    def get_tensorrt(self):
        if self.__tensorrt: return self.__tensorrt.__version__
    
    def get_ncnn(self):
        if self.__ncnn: return self.__ncnn.__version__

    def get_half_precision(self):
        """
        Function that checks if the torch backend supports bfloat16
        """
        if self.pytorch_device == "CPU":
            return False
        try:
            dev = "cuda" if self.pytorch_device == "rocm" else self.pytorch_device.lower()
            x = self.__torch.tensor([1.0], dtype=self.__torch.float16).to(device=dev)
            return True
        except Exception as e:
            return False    
    
    def get_gpus_torch(self):
        """
        Function that returns a list of available GPU names using PyTorch.
        """
        devices = []
        if self.__torch:
            if self.pytorch_device == "CPU": return ["CPU"]
            if self.pytorch_device.lower() == "mps": return ["Apple MPS"]
            torch_cmd_dict = {
            "cuda": self.__torch.cuda,
            "xpu": self.__torch.xpu,
            "rocm": self.__torch.cuda,
            }
            try:
                torch_cmd = torch_cmd_dict.get(self.pytorch_device.lower())
                if torch_cmd is not None and torch_cmd.is_available():
                    for dev_index in range(torch_cmd.device_count()):
                        props = torch_cmd.get_device_properties(dev_index)
                        devices.append(props.name)
            except Exception:
                pass
            if not devices:
                devices.append("CPU")
        if not devices:
            devices.append("CPU")
        return devices

    def get_gpus_ncnn(self):
        if self.__ncnn:
            from ..constants import PLATFORM
            if PLATFORM == "win32":
                # this is to prevent ncnn from creating a crashdump file on windows, despite working.
                # Dont know the side effects of this, but if there are thats for a later me to figure out.
                try:
                    import ctypes
                    SEM_NOGPFAULTERRORBOX = 0x0002
                    SEM_FAILCRITICALERRORS = 0x0001

                    ctypes.windll.kernel32.SetErrorMode(
                        SEM_FAILCRITICALERRORS | SEM_NOGPFAULTERRORBOX
                    )
                except Exception as e:
                    log_error(str(e))
            devices = []
            try:
                with suppress_stdout_stderr():

                    gpu_count = self.__ncnn.get_gpu_count()
                    if gpu_count < 1:
                        return ["CPU"]
                    for i in range(gpu_count):
                        device = self.__ncnn.get_gpu_device(i)
                        gpu_info = device.info()
                        devices.append(gpu_info.device_name())
                return devices
            except Exception:
                return ["CPU"]
            except Exception as e:
                log_error(str(e))
                return "Unable to get NCNN GPU"