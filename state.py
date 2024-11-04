import ctypes
from ctypes import wintypes
import logging
import os
import json
from key_map import prom_keys, prom_keys_include_enter

logging.basicConfig(filename='keyboard_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# 설정 파일 경로
CONFIG_FILE = 'config.json'

user32 = ctypes.WinDLL('user32', use_last_error=True)

LoadKeyboardLayout = user32.LoadKeyboardLayoutW
LoadKeyboardLayout.argtypes = [wintypes.LPCWSTR, wintypes.UINT]
LoadKeyboardLayout.restype = wintypes.HKL

KOREAN_LAYOUT_ID = "00000412"  # 한국어 (Microsoft IME)
ENGLISH_LAYOUT_ID = "00000409"  # 영어 (미국)

monitoring = False
collected_keys = []
chatingchang = False
toggle_key = None
start_key = 'enter'  # 기본값
end_key = '\\'
cursor_enable = False # 기본값

def load_config():
    global config, start_key, end_key, toggle_key, chatingchang
    if not os.path.exists(CONFIG_FILE):
        logging.warning(f"설정 파일 '{CONFIG_FILE}'가 존재하지 않습니다. ")
        logging.info(f"기본값 : {start_key=}, {end_key=}, {toggle_key=}")
        return
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)

            temp_start_key = config.get('start_key', start_key)
            temp_end_key = config.get('end_key', end_key)
            if temp_start_key in prom_keys:
                logging.warning(f"{temp_start_key}는 사용할 수 없는 키입니다.")
            else:
                start_key = temp_start_key
            if temp_end_key in prom_keys_include_enter:
                logging.warning(f"{temp_end_key}는 사용할 수 없는 키입니다.")
            else:
                end_key = temp_end_key

            if start_key == end_key:
                toggle_key = start_key
                start_key = None
                end_key = None
    except Exception as e:
        logging.error(f"설정 파일 로드 중 오류 발생: {e}")
        print(f"설정 파일 로드 중 오류 발생: {e}")
    logging.info(f"config 파일 로드 : {start_key=}, {end_key=}, {toggle_key=}")