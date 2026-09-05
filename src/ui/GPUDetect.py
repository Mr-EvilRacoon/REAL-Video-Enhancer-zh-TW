try:
    from ..constants import PLATFORM 
    from ..Util import log
except Exception:
    PLATFORM = 'win32'
    def log(msg): print(msg)
import subprocess
import re

class GPUDetect:
    def __init__(self):
        self.gpu_info = self.get_gpu_info()

    def get_gpu_info(self):
        """Retrieve GPU info via platform-appropriate method."""
        if PLATFORM == "win32":
            # Try nvidia-smi first
            try:
                output = subprocess.check_output(
                    "nvidia-smi", shell=True
                ).decode()
                return str(output.strip().split("\n"))
            except Exception:
                pass
            # Fallback: use WMI to get GPU name
            try:
                output = subprocess.check_output(
                    'wmic path win32_VideoController get name',
                    shell=True
                ).decode()
                return output.strip()
            except Exception:
                return "Unable to retrieve GPU info on Windows"

        elif PLATFORM == "darwin":  # macOS
            try:
                output = subprocess.check_output(
                    "system_profiler SPDisplaysDataType | grep Vendor", shell=True
                ).decode()
                return output.strip().split(":")[1].strip()
            except Exception:
                return "Unable to retrieve GPU info on macOS"

        elif PLATFORM == "linux":
            try:
                # Try lspci command first
                output = subprocess.check_output("lspci | grep -i vga", shell=True).decode()
                return output.strip().split(":")[2].strip()
            except Exception:
                try:
                    # If lspci fails, try reading from /sys/class/graphics
                    with open("/sys/class/graphics/fb0/device/vendor", "r") as f:
                        vendor_id = f.read().strip()
                    return f"Vendor ID: {vendor_id}"
                except Exception:
                    return "Unable to retrieve GPU info on Linux"

        else:
            return "Unsupported operating system"


    def getVendor(self):
        """
        Gets GPU vendor of the system
        vendors = ["Intel", "AMD", "Nvidia"]
        """
        vendors = ["Intel", "AMD", "Nvidia"]
        for vendor in vendors:
            if vendor.lower() in self.gpu_info.lower():
                return vendor
        return None
    
    def getModelOfGPU(self):
        vendor = self.getVendor()
        model = "0"
        if vendor == "Nvidia":
            try:
                model = re.findall(r"RTX \d\d\d\d", self.gpu_info)[0]
                log("GPU Model Found: " + vendor + " " + model)
            except Exception:
                log("Couldnt find gpu model, " + self.gpu_info)
        elif vendor == "AMD":
            # Try to extract AMD GPU model (e.g., RX 9060 XT, RX 7900 XTX)
            try:
                match = re.search(r'(RX\s*\d{4}\s*\w*|Radeon\s*\w+)', self.gpu_info)
                if match:
                    model = match.group(0).strip()
                    log("GPU Model Found: " + vendor + " " + model)
                else:
                    model = "AMD"
                    log("AMD GPU detected, model unknown: " + self.gpu_info)
            except Exception:
                model = "AMD"
        elif vendor == "Intel":
            # Intel Arc or integrated graphics
            try:
                match = re.search(r'(Arc\s*\w+|UHD\s*\w+|Iris\s*\w+)', self.gpu_info)
                if match:
                    model = match.group(0).strip()
                else:
                    model = "Intel"
                log("GPU Model Found: " + vendor + " " + model)
            except Exception:
                model = "Intel"
        return model
    
    def getPyTorchFeatures(self) -> str | None:
        """
        Detect available PyTorch backend based on GPU vendor and model.
        Returns: "cuda", "rocm", "xpu", or None
        """
        vendor = self.getVendor()
        model = self.getModelOfGPU()
        
        if vendor == "Nvidia":
            # NVIDIA RTX 2000+ supports CUDA
            try:
                if int(model[4]) >= 2:
                    return "cuda"
            except (IndexError, ValueError):
                pass
            return None
        
        elif vendor == "AMD":
            # AMD GPUs with ROCm support (RX 5000+ / RDNA2+)
            # Check for ROCm-supported AMD GPUs
            try:
                # RX 5000 series (RDNA), RX 6000 (RDNA2), RX 7000/9000 (RDNA3/4)
                rx_match = re.search(r'RX\s*(\d{4})', model)
                if rx_match:
                    rx_model_num = int(rx_match.group(1))
                    # RX 9000/7000 (RDNA 3/4) - ROCm 7.1+ on Windows
                    # RX 6000 (RDNA 2) - ROCm on Linux
                    # RX 5000 (RDNA 1) - Limited ROCm
                    if rx_model_num >= 5000:
                        return "rocm"
                # Check for Radeon Pro / Instinct (datacenter GPUs)
                if "Radeon" in model or "Instinct" in model:
                    return "rocm"
            except Exception:
                pass
            # Fallback: if AMD is detected but model unclear, offer ROCm
            return "rocm"
        
        elif vendor == "Intel":
            # Intel Arc and newer integrated graphics support XPU
            try:
                # Intel Arc series
                if "Arc" in model:
                    return "xpu"
                # Intel UHD 700+ / Iris Xe (Tiger Lake+)
                uhd_match = re.search(r'UHD\s*(\d+)', model)
                if uhd_match:
                    uhd_num = int(uhd_match.group(1))
                    if uhd_num >= 700:
                        return "xpu"
                # If Intel GPU detected, default to XPU
                return "xpu"
            except Exception:
                return "xpu"
        
        return None
    
if __name__ == '__main__':
    print(GPUDetect().getPyTorchFeatures())