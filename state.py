import keyboard
import exec_once
from overlay import OverlayWindow
from time import sleep
from eng_kor_converter import engkor, SHIFT_KEYS

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
        hud_size, do_update = exec_once.read_json()

        # logistic regression
        offset_x = -22.90 * hud_size + 99.93
        offset_y = -12.50 * hud_size + 99.775
        
        self.overlay = OverlayWindow(offset_x, offset_y, hud_size)
        # ==================================================================
        print("https://github.com/amature0000/engkor_converter")
        if do_update: exec_once.print_latest_release()
    # ==============================================================================================
    def clear(self, show_overlay=False):
        self.fixed_keys = ''
        self.korean_keys.clear()
        if show_overlay: self.show_overlay()
        else: self.overlay.root.withdraw() # hide overlay
        
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
    # ==============================================================================================
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
"""
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

def chmod(self):
    self.mode = not self.mode
    self.show_overlay()
"""
