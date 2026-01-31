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
            self._backspace()
        elif text == 'space':
            self._insert(' ')
        elif len(text) == 1:
            self._insert(text)

    def process(self, placeholder = False):
        cursor = self._eng_to_kor()
        string = self.fixed_keys + cursor
        if placeholder and (not string): 
            string = 'Press \"\\\" key to send the message'
            if self.mode: string = '전송하려면 \"\\\" 키 입력'
        return string
    
    def clear(self):
        self.fixed_keys = ''
        self.korean_keys.clear()
    # ==============================================================================================        
    def _backspace(self):
        if len(self.korean_keys) > 0:
            self.korean_keys.pop()
        else:
            self.fixed_keys = self.fixed_keys[:-1]

    def _insert(self, word:str):
        if self.mode:
            if word not in SHIFT_KEYS: word = word.lower()
            self.korean_keys.append(word)
        else:
            cursor = self._eng_to_kor()
            self.fixed_keys += cursor + word
            self.korean_keys.clear()

    # NOTE: 해당 함수는 내부에서 fixed_keys를 수정하므로, caller는 fixed_keys와 이 함수를 원자적으로 접근하면 안 됨
    def _eng_to_kor(self):
        if len(self.korean_keys) == 0: return ''
        temp_korean_keys = ''.join(self.korean_keys)

        fixed_str, cursor, split_index = engkor(temp_korean_keys)

        self.fixed_keys += fixed_str
        self.korean_keys = self.korean_keys[split_index:]
        return cursor

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