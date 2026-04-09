from eng_kor_converter import engkor
from time import sleep
import keyboard
from pathlib import Path
import json
import os

appdata = Path(os.environ.get("APPDATA", "")) / "EKconverter"
appdata.mkdir(exist_ok=True)
cfg = appdata / 'config.json'

SHIFT_KEYS = {'R', 'E', 'Q', 'T', 'W', 'O', 'P'}
EK_KEYS = {'right alt', 'alt', 'hangeul'}
DELAY = 10 # ms

class State:
    def __init__(self):
        self.mode = True # True: kor, False: eng

        self.special_keys = {
            'space': self._handle_space,
            'backspace': self._handle_backspace
        }
        self.korean_keys = []
        self.kstring_before = ""

        self.delay = DELAY
        try:
            with open(cfg, 'r', encoding='utf-8') as f:
                config = json.load(f)
                self.delay = int(config.get('delay', DELAY))
        except Exception: pass
    # ==============================================================================================
    def process(self, text):
        # 키보드 이벤트 누적
        result = self._record(text)
        # 상태 업데이트
        back, kstring = self._update_state()

        if back:
            keyboard.press_and_release("backspace")
            sleep(self.delay / 1000)

        if kstring:
            keyboard.write(kstring, delay=0.01)
            
        return result

    def clear(self):
        self.korean_keys.clear()
        self.kstring_before = ""
    # ==============================================================================================
    def _record(self, text : str):
        if text in EK_KEYS:
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
            return True
        return False

    def _update_state(self):
        if len(self.korean_keys) == 0: return False, ""

        # 한글 문자열 계산
        kstring, split_index = engkor(''.join(self.korean_keys))
        
        # 확정된 한글 문자열에 대응되는 korean_keys 제거
        self.korean_keys = self.korean_keys[split_index:]

        # 이전 한글 문자열과 비교해 최종 한글 문자열 계산
        result, kstring = self._calculate_diff(kstring)
        return result, kstring

    def _calculate_diff(self, kstring):
        result = True
        # 최초 상태에서 전이 시 
        if not self.kstring_before: result = False

        # index 0의 글자가 변화했는지 검사
        elif kstring.startswith(self.kstring_before):
            kstring = kstring[1:]
            result = False

        # 이전 상태 저장
        if kstring:
            self.kstring_before = kstring[-1]
        return result, kstring
    # ==============================================================================================
    def change_delay(self):
        self.delay = self.delay + int(DELAY/10)
        if self.delay > DELAY * 2: self.delay = DELAY
        with open(cfg, 'w') as f:
            json.dump({'delay': self.delay}, f)