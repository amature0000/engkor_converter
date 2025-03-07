import win32gui
from time import sleep
from os import system

def get_window_rect(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        print(f"{title} 창을 찾을 수 없습니다. 검색 중...")
        while hwnd == 0:
            print('.')
            sleep(1)
            hwnd = win32gui.FindWindow(None, title)
        system('cls')
    return win32gui.GetWindowRect(hwnd)



import re
from requests import get


# 업데이트 시 변경
VER = "3.12"
OWNER = "amature0000"
REPO = "engkor_converter"
    
def print_latest_release():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"
    response = get(url)

    if response.status_code == 200:
        data = response.json()
        latest_version = data.get("tag_name")
        release_notes = data.get("body")
        if latest_version and release_notes:            
            release_notes = re.sub(r'^.*## 변경사항', '', release_notes, flags=re.DOTALL)
            release_notes = re.sub(r'## 다운로드 파일.*$', '', release_notes, flags=re.DOTALL)
            release_notes = release_notes.strip()
            if VER != latest_version:
                print(f'\n\n신규 릴리즈가 있습니다! (현재 버전){VER} -> (최신 버전){latest_version}\n\n수정사항:\n{release_notes}')
            return
    print("\n\n오류: 릴리즈를 확인할 수 없습니다.")