; REAL Video Enhancer - Traditional Chinese Edition Installer

!include "MUI2.nsh"
!include "logiclib.nsh"

!define NAME "REAL Video Enhancer"
!define APPFILE "REAL-Video-Enhancer.exe"
!define VERSION "2.4.1-zh-TW"
!define COMPANYNAME "TNTwise"
!define VERSIONMAJOR 2
!define VERSIONMINOR 4
!define VERSIONBUILD 1
!define DISPLAYVERSION "2.4.1"
!define INSTALLSIZE 297000

Name "${NAME} ${VERSION}"
OutFile "REAL-Video-Enhancer-${VERSION}-Windows-Setup_x86_64.exe"
InstallDir "$PROGRAMFILES\${NAME}"
InstallDirRegKey HKCU "Software\${NAME}" ""
RequestExecutionLevel admin

!define MUI_ICON "icons/logo-v2.ico"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "LICENSE"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

Section "install"
    SectionIn RO
    SetOutPath "$INSTDIR"
    File /r "dist\REAL-Video-Enhancer\*.*"
    File /r "icons\logo-v2.ico"
    
    createDirectory "$COMMONSMPROGRAMS\${COMPANYNAME}"
    createShortCut "$COMMONSMPROGRAMS\${COMPANYNAME}\${NAME}.lnk" "$INSTDIR\REAL-Video-Enhancer.exe" "" "$INSTDIR\logo-v2.ico"
    writeUninstaller "$INSTDIR\Uninstall.exe"
    RMDir /r "$INSTDIR\backend"

    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "DisplayName" "${NAME} ${VERSION}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "UninstallString" '"$INSTDIR\uninstall.exe"'
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "QuietUninstallString" '"$INSTDIR\uninstall.exe" /S'
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "InstallLocation" '"$INSTDIR"'
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "DisplayIcon" '"$INSTDIR\logo-v2.ico"'
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "DisplayVersion" "${VERSION}"
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "VersionMajor" ${VERSIONMAJOR}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "VersionMinor" ${VERSIONMINOR}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "NoRepair" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}" "EstimatedSize" ${INSTALLSIZE}
SectionEnd

Section "Desktop Shortcut" DeskShort
    CreateShortCut "$COMMONDESKTOP\${NAME}.lnk" "$INSTDIR\${APPFILE}"
SectionEnd

Section "Uninstall"
    Delete "$COMMONDESKTOP\${NAME}.lnk"
    Delete "$COMMONSMPROGRAMS\${COMPANYNAME}\${NAME}.lnk"
    RMDir "$COMMONSMPROGRAMS\${COMPANYNAME}"
    Delete "$INSTDIR\Uninstall.exe"
    RMDir /r "$INSTDIR"
    RMDir /r "$LOCALAPPDATA\REAL-Video-Enhancer"
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${NAME}"
SectionEnd
