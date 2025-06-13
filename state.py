import keyboard
import exec_once
from time import sleep

class State:
    def __init__(self):
        self.hud_size, do_update = exec_once.read_json()

        # logistic regression
        self.offset_x = -22.90 * self.hud_size + 99.93
        self.offset_y = -12.50 * self.hud_size + 99.775

        # ==================================================================
        print("https://github.com/amature0000/engkor_converter")
        if do_update: exec_once.print_latest_release()
    # ==============================================================================================
    def process_and_insert(self, text):
        # 한글 문자열 타이핑
        keyboard.press('esc')
        sleep(0.05)
        keyboard.release('esc')
        keyboard.press('enter')
        sleep(0.05)
        keyboard.release('enter')
        if len(text) > 0:
            sleep(0.1)
            keyboard.write(text, delay=0.01)
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