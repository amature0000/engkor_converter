from win32gui import FindWindow, GetWindowRect
from time import sleep
import os
import keyboard
import json
from pathlib import Path
from PIL import ImageColor
import colorama

colorama.init()
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
    text = _convert_script(text)

    # 한글 문자열 타이핑
    simulate_key_process('enter')
    keyboard.write(text, delay=0.01)
    sleep(0.01)
    simulate_key_process('enter')

def _tohex(name):
    r, g, b = ImageColor.getrgb(name)
    return f"{r:02X}{g:02X}{b:02X}"

def _convert_script(text: str):
    parts = text.split("#")
    if len(parts) == 1: return text
    result = []

    # 첫 문장이 #로 시작한다면 -> parts[0] == ""
    if parts[0]:
        result.append(parts[0])

    for part in parts[1:]:
        tokens = part.split(maxsplit=1)

        color_name = tokens[0]
        content = tokens[1] if len(tokens) > 1 else ""

        try:
            hex6 = _tohex(color_name)
            result.append(f"<c=FF{hex6}>{content}")
        except ValueError:
            result.append(part)

    return "".join(result)

def color_iterator():
    names = sorted(ImageColor.colormap.keys())
    for i in range(0, len(names), 15): yield names[i:i+20]
color_it = color_iterator()    

def print_colors():    
    try:
        for name in next(color_it): 
            r, g, b = ImageColor.getrgb(name)
            print(f"\033[38;2;{r};{g};{b}m{name}\033[0m\tRGB:({r}, {g}, {b})")
        print(f"계속해서 보려면 End 키 입력")
    except StopIteration:
        print("모든 색상을 출력했습니다.")

print_colors()
print_colors()

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
    print("EKconverter ver 3.15.0")
    print("Home 키를 눌러 HUD 크기 변경")
    print("End 키를 눌러 색상 테이블 보기")
    return hud_size

def save_json(hud):
    with open(cfg, 'w') as f:
        json.dump({'hud_size': hud}, f)