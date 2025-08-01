[Setup]
AppName=EKconverter
AppVersion=1.0.0
DefaultDirName={pf}\EKconverter
DefaultGroupName=EKconverter
OutputBaseFilename=EKconverterSetup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin

[Files]
Source: "python_embed\*"; DestDir: "{app}\python"; Flags: recursesubdirs
Source: "source\*";       DestDir: "{app}\source"; Flags: recursesubdirs
Source: "tk_embed\tcl\*"; DestDir: "{app}\python\tcl"; Flags: recursesubdirs
Source: "tk_embed\DLLs\*"; DestDir: "{app}\python\DLLs"; Flags: recursesubdirs
Source: "tk_embed\tkinter\*"; DestDir: "{app}\python\Lib\tkinter"; Flags: recursesubdirs
Source: "source\config.json"; DestDir: "{userappdata}\EKconverter"; Flags: recursesubdirs

[Run]
; 1) pip 설치
Filename: "{app}\python\python.exe"; Parameters: "get-pip.py --quiet"; WorkingDir: "{app}\python"; StatusMsg: "pip 설치 중..."

; 2) 라이브러리 설치 (임베디드 Lib 폴더에 설치)
Filename: "{app}\python\python.exe"; Parameters: "-m pip install --upgrade pip"; WorkingDir: "{app}\python"; StatusMsg: "pip 업데이트 중..."
Filename: "{app}\python\python.exe"; Parameters: "-m pip install -r ""{app}\source\requirements.txt"" --target ""{app}\python\Lib\site-packages"""; WorkingDir: "{app}\python"; StatusMsg: "요구 라이브러리 설치 중..."

[Icons]
Name: "{userdesktop}\EKconverter"; Filename: "{app}\python\python.exe"; Parameters: """{app}\source\runme.py"""; WorkingDir: "{app}\source"; IconFilename: "{app}\source\favicon.ico"
