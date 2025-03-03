import keyboard
from overlay import OverlayWindow
from json import load
from time import sleep
from eng_kor_converter import engkor
from exec_once import get_latest_release

# 업데이트 시 변경
VER = "3.11"
CONFIG_FILE = 'config.json'
# shift keys
SHIFT_KEYS = {'R', 'E', 'Q', 'T', 'W', 'O', 'P'}

    
class State:
    def __init__(self):
        self.typing = False
        self.mode = True # True: kor, False: eng
        self.fixed_keys = ''
        self.korean_keys = []
        self.start_key = 'enter'
        self.end_key = '\\'
        self.exit_key = 'esc'
        self.engkor_key = ['right alt', 'alt']
        # chatbox
        hud_size = 0.9
        offset_x = 79.35
        offset_y = 88.5
        # do_update
        do_update = True
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = load(f)
                hud_size = config.get('hud_size', hud_size)
                do_update = bool(config.get('get_latest_update', do_update))
        except Exception as e: pass
        if hud_size == 0.75:
            offset_x = 82.75
            offset_y = 90.4
        elif hud_size == 0.8:
            offset_x = 81.65
            offset_y = 89.75
        elif hud_size == 0.85:
            offset_x = 80.4
            offset_y = 89.2
        else: # hud_size == 0.9
            offset_x = 79.35
            offset_y = 88.5
            hud_size = 0.9
        
        # overlay object
        self.overlay = OverlayWindow(offset_x, offset_y, hud_size)
        
        print("https://github.com/amature0000/engkor_converter")
        if do_update:
            latest_version, patch_note = get_latest_release()
            if VER != latest_version:
                print(f'\n\n신규 릴리즈가 있습니다! (현재 버전){VER} -> (최신 버전){latest_version}\n\n수정사항:\n{patch_note}')
    # ==============================================================================================
    def clear(self, show_overlay=False):
        self.fixed_keys = ''
        self.korean_keys.clear()
        if show_overlay: self.show_overlay()
        else: self.hide_overlay()
        
    def chmod(self):
        self.mode = not self.mode
        self.show_overlay()
        
    def backspace(self):
        if len(self.korean_keys) > 0:
            self.korean_keys.pop()
        else:
            self.fixed_keys = self.fixed_keys[:-1]
        self.show_overlay()

    def insert(self, word:str):
        if self.mode:
            if word not in SHIFT_KEYS: word = word.lower()
            self.korean_keys.append(word)
        else:
            self.eng_to_kor(True)
            self.fixed_keys = self.fixed_keys + word
        self.show_overlay()

    def eng_to_kor(self, collapse = False): # if collapse: return None
        if len(self.korean_keys) == 0: return ''
        temp_korean_keys = ''.join(self.korean_keys)
        if collapse:
            fixed_str = engkor(temp_korean_keys, collapse)
            self.fixed_keys += fixed_str
            self.korean_keys.clear()
            return
        fixed_str, temp_str, split_index = engkor(temp_korean_keys)
        self.fixed_keys += fixed_str
        self.korean_keys = self.korean_keys[split_index:]
        return temp_str
    # ==============================================================================================   
    def show_overlay(self):
        temp_str = self.eng_to_kor()
        temp_string = self.fixed_keys
        if temp_str: temp_string += temp_str
        if not temp_string: 
            temp_string = 'Press \"\\\" key to send the message'
            if self.mode: temp_string = '전송하려면 \"\\\" 키 입력'
        self.overlay.show_message(temp_string)

    def hide_overlay(self):
        self.overlay.hide_message()
    # ==============================================================================================
    # from utils.py(legacy)
    def start_typing(self):
        self.typing = True
        self.clear(True)

    def end_typing(self):
        if not self.typing: return
        self.process_and_insert()
        self.typing = False
        self.clear()

    def exit_typing(self):
        self.typing = False
        self.clear()

    def process_and_insert(self):
        self.eng_to_kor(True)
        # 기존 입력 삭제
        keyboard.press('esc')
        sleep(0.05)
        keyboard.release('esc')
        keyboard.press('enter')
        sleep(0.05)
        keyboard.release('enter')
        # 한글 문자열 타이핑
        if len(self.fixed_keys) > 0:
            sleep(0.1)
            keyboard.write(self.fixed_keys, delay=0.01)
        # 텍스트 전송
        keyboard.press('enter')
        sleep(0.05)
        keyboard.release('enter')

"""
휴리스틱한 값들..

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