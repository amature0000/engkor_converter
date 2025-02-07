from overlay import OverlayWindow
import os
import json
from eng_kor_converter import engkor

CONFIG_FILE = 'config.json'

class State:
    def __init__(self):
        self.typing = False
        self.mode = True # True: kor, False: eng
        self.fixed_keys = []
        self.korean_keys = []
        self.start_key = 'enter'
        self.end_key = '\\'
        self.exit_key = 'esc'
        self.engkor_key = ['right alt', 'alt']
        # default
        self.offset_x = 79.35
        self.offset_y = 88.5
        self.hud_size = 0.9
        if not os.path.exists(CONFIG_FILE):
            print(f"설정 파일 '{CONFIG_FILE}' 없음. 기본값으로 실행 : hud_size = 0.9")
        else: 
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # read hud_size
                    self.hud_size = config.get('hud_size', self.hud_size)
                    if self.hud_size == 0.75:
                        self.offset_x = 82.75
                        self.offset_y = 90.4
                    elif self.hud_size == 0.8:
                        self.offset_x = 81.65
                        self.offset_y = 89.75
                    elif self.hud_size == 0.85:
                        self.offset_x = 80.4
                        self.offset_y = 89.2
                    else:
                        self.offset_x = 79.35
                        self.offset_y = 88.5
                        self.hud_size = 0.9
                    print(f"설정 파일 로드 완료 : hud_size = {self.hud_size}")
            except Exception as e:
                print(f"설정 파일 로드 중 오류 발생")
                
        self.overlay = OverlayWindow(self.offset_x, self.offset_y, self.hud_size)
    
    def backspace(self):
        if len(self.korean_keys) > 0:
            self.korean_keys.pop()
        else:
            self.fixed_keys.pop()

    def put(self, word=''):
        self.fixed_keys = self.fixed_keys + list(self.eng_to_kor())
        self.fixed_keys.append(word)
        self.korean_keys = []
        
    def insert(self, word):
        if self.mode:
            self.korean_keys.append(word)
        else:
            self.fixed_keys.append(word)

    def eng_to_kor(self) -> list:
        temp = ''.join(self.korean_keys)
        result = engkor(temp)
        return result
    
    def show_overlay(self):
        temp_String = ''.join(self.fixed_keys) + self.eng_to_kor()
        if temp_String == '': temp_String = ' \"\\\" 키를 눌러 입력 완료'
        self.overlay.show_message(temp_String)

    def hide_overlay(self):
        self.overlay.hide_message()

    def init_print(self):
        print("https://github.com/amature0000/engkor_converter \n종료하려면 창을 닫으세요.\n")


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