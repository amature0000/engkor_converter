from overlay import OverlayWindow
import os
import json
from eng_kor_converter import engkor
from key_map import shift_keys
from track_releases import get_latest_release

# 업데이트 시 변경
VER = 3.8
CONFIG_FILE = 'config.json'

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
        # default
        self.offset_x = 79.35
        self.offset_y = 88.5
        self.hud_size = 0.9
        # noupdate
        self.do_update = True
        # update_log
        self.current_version = str(VER)
        self.latest_version = str(VER) # will be changed via get_latest_release()
        self.patch_note = ''
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.hud_size = config.get('hud_size', self.hud_size)
                self.do_update = config.get('get_latest_update', self.do_update)
        except Exception as e: pass
        if self.hud_size == 0.75:
            self.offset_x = 82.75
            self.offset_y = 90.4
        elif self.hud_size == 0.8:
            self.offset_x = 81.65
            self.offset_y = 89.75
        elif self.hud_size == 0.85:
            self.offset_x = 80.4
            self.offset_y = 89.2
        else: # hud_size == 0.9
            self.offset_x = 79.35
            self.offset_y = 88.5
            self.hud_size = 0.9
        
        self.overlay = OverlayWindow(self.offset_x, self.offset_y, self.hud_size)
        
        if self.do_update:
            self.latest_version, self.patch_note = get_latest_release()
        if self.current_version == self.latest_version:
            self.update_message = ''
        else:
            self.update_message = f'\n신규 릴리즈가 있습니다! (현재 버전){self.current_version} -> (최신 버전){self.latest_version}\n수정사항:\n{self.patch_note}\n'
    
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
            if word not in shift_keys: word = word.lower()
            self.korean_keys.append(word)
        else:
            self.eng_to_kor(True)
            self.fixed_keys = self.fixed_keys + word
        self.show_overlay()

    def eng_to_kor(self, collapse = False) -> str:
        if len(self.korean_keys) == 0: return ''
        elif collapse:
            fixed_str, _, split_index = engkor(''.join(self.korean_keys), collapse)
            self.fixed_keys += fixed_str
            self.korean_keys.clear()
            return ''
        else:
            fixed_str, temp_str, split_index = engkor(''.join(self.korean_keys))
            self.fixed_keys += fixed_str
            self.korean_keys = self.korean_keys[split_index:]
            return temp_str
    
    def show_overlay(self):
        temp_str = self.eng_to_kor()
        temp_string = self.fixed_keys
        if temp_str: temp_string += temp_str
        if not temp_string: 
            if self.mode: temp_string = ' \"\\\" 키를 눌러 전송'
            else: temp_string = 'Press \"\\\" key to send the message'
        self.overlay.show_message(temp_string)

    def hide_overlay(self):
        self.overlay.hide_message()

    def init_print(self):
        os.system('cls')
        print(f"https://github.com/amature0000/engkor_converter \n{self.update_message}")


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