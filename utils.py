import re
from win32gui import FindWindow, GetWindowRect
from time import sleep
import keyboard
from os import system
from requests import get
from json import load

def process_and_insert(text):
    # 한글 문자열 타이핑
    if len(text) > 0:
        sleep(0.1)
        keyboard.write(text, delay=0.01)
    sleep(0.05)
    keyboard.press('enter')
    sleep(0.05)
    keyboard.release('enter')

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
    version = "4.0"
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
        if version == latest_version: return
        release_notes = re.sub(r'^.*## 변경사항', '', release_notes, flags=re.DOTALL)
        release_notes = re.sub(r'## 다운로드 파일.*$', '', release_notes, flags=re.DOTALL)
        release_notes = release_notes.strip()
        print(f'\n\n신규 릴리즈가 있습니다! (현재 버전){version} -> (최신 버전){latest_version}\n\n수정사항:\n{release_notes}')

def read_process_json():
    config_file = 'config.json'
    global read_process_json
    read_process_json = None
    hud_size = 0.9
    do_update = True
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = load(f)
            hud_size = float(config.get('hud_size', 0.9))
            do_update = bool(config.get('get_latest_update', True))
    except Exception: pass
    print("https://github.com/amature0000/engkor_converter")
    if do_update: print_latest_release()

    offset_x = -22.90 * hud_size + 99.93
    offset_y = -12.50 * hud_size + 99.775

    return hud_size, offset_x, offset_y


"""
선형회귀 데이터

# ratio HUD = 0.75
OFFSET_X = 82.75
OFFSET_Y = 90.4

# ratio HUD = 0.8
OFFSET_X = 81.65
OFFSET_Y = 89.75

# ratio HUD = 0.85
OFFSET_X = 80.4
OFFSET_Y = 89.2

# ratio HUD = 0.9
OFFSET_X = 79.35
OFFSET_Y = 88.5
"""