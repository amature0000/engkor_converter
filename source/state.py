from eng_kor_converter import engkor
from time import sleep
import keyboard
from logger import log_mode


def simulate_key_process(key):
    keyboard.press(key)
    sleep(0.05)
    keyboard.release(key)
    sleep(0.05)

def simulate_write_process(text):
    keyboard.write(text, delay=0.01)

# shift keys
SHIFT_KEYS = {'R', 'E', 'Q', 'T', 'W', 'O', 'P'}

class State:
    def __init__(self):
        self.mode = True # True: kor, False: eng

        self.engkor_key = ['right alt', 'alt']
        self.korean_keys = []
        self.fixed = ""
        self.cursor = ""
    # ==============================================================================================
    @log_mode
    def record(self, text):
        if text in self.engkor_key:
            self.mode = not self.mode
            self.clear()
            return False
        if self.mode == False:
            return True
        # -----------------------
        if text == 'space':
            self.clear()
            return True
        elif text == 'backspace':
            self._backspace()
        elif len(text) == 1:
            self._insert(text)
        return False
    
    def clear(self):
        self.korean_keys.clear()
        self.fixed = ""
        self.cursor = ""

    def write(self):
        if self.cursor != "":
            simulate_key_process("backspace")

        delete = self._eng_to_kor()

        if delete:
            simulate_write_process(self.cursor)
        else:
            simulate_write_process(self.fixed + self.cursor)
    # ==============================================================================================        
    def _backspace(self):
        if self.korean_keys:
            self.korean_keys.pop()
        if not self.korean_keys:
            self.clear()
            simulate_key_process("backspace")

    def _insert(self, word:str):
        if word not in SHIFT_KEYS: word = word.lower()
        self.korean_keys.append(word)

    def _eng_to_kor(self):
        if len(self.korean_keys) == 0: return False
        temp_korean_keys = ''.join(self.korean_keys)

        self.fixed, self.cursor, split_index = engkor(temp_korean_keys)

        self.korean_keys = self.korean_keys[split_index:]
        return split_index == 0