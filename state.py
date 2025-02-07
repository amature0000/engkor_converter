from overlay import OverlayWindow
import threading
from eng_kor_converter import engkor

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
        self.overlay = OverlayWindow()
    
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
        if temp_String == '': temp_String = '\\ 키를 눌러 입력 완료'
        self.overlay.show_message(temp_String)

    def hide_overlay(self):
        self.overlay.hide_message()

    def init_print(self):
        print("https://github.com/amature0000/engkor_converter \n종료하려면 창을 닫으세요.\n")