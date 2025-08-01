from win32gui import FindWindow, GetWindowRect
from time import sleep
import os
import keyboard
import re
from requests import get
import json
from pathlib import Path

appdata = Path(os.environ.get("APPDATA", "")) / "EKconverter"
appdata.mkdir(exist_ok=True)
cfg = appdata / 'config.json'

def simulate_key_process(key):
    keyboard.press(key)
    sleep(0.05)
    keyboard.release(key)
    sleep(0.05)

def process_and_insert(text):
    simulate_key_process('esc')
    if not text: return

    # 한글 문자열 타이핑
    simulate_key_process('enter')
    keyboard.write(text, delay=0.01)
    sleep(0.01)
    simulate_key_process('enter')

def get_window_rect():
    game_title = "HELLDIVERS™ 2"
    global get_window_rect
    get_window_rect = None

    print(f"{game_title} 창을 찾을 수 없습니다. 검색 중...")
    while (hwnd:=FindWindow(None, game_title)) == 0:
        print('.')
        sleep(1)
    os.system('cls')
    return GetWindowRect(hwnd)

def _print_latest_release():
    version = "(legacy)ver 3"
    owner = "amature0000"
    repo = "engkor_converter"
    global _print_latest_release
    _print_latest_release = None

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
        print(f'\n\n(현재 버전){version} -> (최신 버전){latest_version}\n\n수정사항:\n{release_notes}')

def read_json():
    global read_json
    read_json = None
    hud_size = 0.9
    do_update = True
    try:
        with open(cfg, 'r', encoding='utf-8') as f:
            config = json.load(f)
            hud_size = float(config.get('hud_size', 0.9))
            do_update = bool(config.get('get_latest_update', True))
    except Exception: pass
    print("https://github.com/amature0000/engkor_converter")
    if do_update: _print_latest_release()
    print("Home 키를 눌러 설정값 수정")
    return hud_size

def save_json(hud, update):
    print(hud)
    print(update)
    with open(cfg, 'w') as f:
        json.dump({'hud_size': hud, 'get_latest_update': update}, f)