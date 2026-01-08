from win32gui import FindWindow, GetWindowRect
from time import sleep
import os
import keyboard
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

def read_json():
    global read_json
    read_json = None
    hud_size = 0.9
    try:
        with open(cfg, 'r', encoding='utf-8') as f:
            config = json.load(f)
            hud_size = float(config.get('hud_size', 0.9))
    except Exception: pass
    print("https://github.com/amature0000/engkor_converter")
    print("EKconverter ver 3.15")
    print("Home 키를 눌러 HUD 크기 변경")
    return hud_size

def save_json(hud):
    with open(cfg, 'w') as f:
        json.dump({'hud_size': hud}, f)