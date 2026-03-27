from eng_kor_converter import engkor
from time import sleep
import keyboard


# shift keys
SHIFT_KEYS = {'R', 'E', 'Q', 'T', 'W', 'O', 'P'}
DELAY = 0.01

class State:
    def __init__(self):
        self.mode = True # True: kor, False: eng

        self.engkor_keys = ['right alt', 'alt']
        self.special_keys = {
            'space': self._handle_space,
            'backspace': self._handle_backspace
        }
        self.korean_keys = []
        self.cursor = ""
        self.cursor_before = ""
    # ==============================================================================================
    def process(self, text):
        result = self._record(text)
        self._update_state()

        if self.cursor:
            keyboard.write(self.cursor, delay=0.01)
            
        return result

    def clear(self):
        self.korean_keys.clear()
        self.cursor_before = ""
        self.cursor = ""
    # ==============================================================================================
    def _record(self, text : str):
        if text in self.engkor_keys:
            self.mode = not self.mode
            self.clear()
            return False
        
        if self.mode == False:
            return True
        # -----------------------
        if text in self.special_keys:
            return self.special_keys[text]()
        
        if len(text) == 1:
            if text not in SHIFT_KEYS: text = text.lower()
            self.korean_keys.append(text)
        return False
    
    def _handle_space(self):
        self.clear()
        return True
    
    def _handle_backspace(self):
        if self.korean_keys:
            self.korean_keys.pop()
        if not self.korean_keys:
            self.clear()
            keyboard.press_and_release("backspace")
        return False

    def _update_state(self):
        if len(self.korean_keys) == 0: return

        self.cursor, split_index = engkor(''.join(self.korean_keys))
        
        self.korean_keys = self.korean_keys[split_index:]

        if self._calculate_diff():
            keyboard.press_and_release("backspace")
            sleep(DELAY)
        if self.cursor:
            self.cursor_before = self.cursor[-1]

    def _calculate_diff(self):
        # 최초 상태에서 전이 시 
        if not self.cursor_before: return False

        # index 0의 글자가 변화했는지 검사
        if self.cursor.startswith(self.cursor_before):
            self.cursor = self.cursor[1:]
            return False
        return True