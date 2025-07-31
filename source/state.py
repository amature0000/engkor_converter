from eng_kor_converter import engkor

CONFIG_FILE = 'config.json'
# shift keys
SHIFT_KEYS = {'R', 'E', 'Q', 'T', 'W', 'O', 'P'}

class State:
    def __init__(self):
        self.mode = True # True: kor, False: eng
        self.engkor_key = ['right alt', 'alt']
        self.fixed_keys = ''
        self.korean_keys = []
    # ==============================================================================================
    def record(self, text):
        if text in self.engkor_key:
            self.mode = not self.mode
        elif text == 'backspace':
            self.backspace()
        elif text == 'space':
            self.insert(' ')
        elif len(text) == 1:
            self.insert(text)

    def process(self):
        temp_str = self.eng_to_kor()
        temp_string = self.fixed_keys
        if temp_str: temp_string += temp_str
        if not temp_string: 
            temp_string = 'Press \"\\\" key to send the message'
            if self.mode: temp_string = '전송하려면 \"\\\" 키 입력'
        return temp_string
    
    def extract(self):
        self.eng_to_kor(True)
        temp = self.fixed_keys
        return temp
    
    def clear(self):
        self.fixed_keys = ''
        self.korean_keys.clear()
    # ==============================================================================================        
    def backspace(self):
        if len(self.korean_keys) > 0:
            self.korean_keys.pop()
        else:
            self.fixed_keys = self.fixed_keys[:-1]

    def insert(self, word:str):
        if self.mode:
            if word not in SHIFT_KEYS: word = word.lower()
            self.korean_keys.append(word)
        else:
            self.eng_to_kor(True)
            self.fixed_keys = self.fixed_keys + word

    def eng_to_kor(self, collapse = False):
        if len(self.korean_keys) == 0: return ''
        temp_korean_keys = ''.join(self.korean_keys)
        fixed_str, temp_str, split_index = engkor(temp_korean_keys, collapse)
        self.fixed_keys += fixed_str

        if collapse: self.korean_keys.clear()
        else: self.korean_keys = self.korean_keys[split_index:]
        return temp_str

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