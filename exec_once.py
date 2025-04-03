import re
from win32gui import FindWindow, GetWindowRect
from time import sleep
from os import system
from requests import get
from json import load

def get_window_rect():
    game_title = "HELLDIVERS™ 2"
    global get_window_rect
    get_window_rect = None

    print(f"{game_title} 창을 찾을 수 없습니다. 검색 중...")
    while (hwnd:=FindWindow(None, game_title)) == 0:
        print('.')
        sleep(1)
    system('cls')
    return GetWindowRect(hwnd)

def print_latest_release():
    version = "3.13"
    owner = "amature0000"
    repo = "engkor_converter"
    global print_latest_release
    print_latest_release = None

    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = get(url)

    if response.status_code != 200:
        print(f"\n\n오류: 릴리즈를 확인할 수 없습니다:{response.status_code}")
        return
    data = response.json()
    latest_version = data.get("tag_name")
    release_notes = data.get("body")
    if latest_version and release_notes:            
        release_notes = re.sub(r'^.*## 변경사항', '', release_notes, flags=re.DOTALL)
        release_notes = re.sub(r'## 다운로드 파일.*$', '', release_notes, flags=re.DOTALL)
        release_notes = release_notes.strip()
        if version == latest_version: return
        print(f'\n\n신규 릴리즈가 있습니다! (현재 버전){version} -> (최신 버전){latest_version}\n\n수정사항:\n{release_notes}')

def read_json():
    config_file = 'config.json'
    global read_json
    read_json = None

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = load(f)
            hud_size = float(config.get('hud_size', 0.9))
            do_update = bool(config.get('get_latest_update', True))
        return hud_size, do_update
    except Exception: pass
    return 0.9, True