import logging
import os
import json
from key_map import start_keys_exception, end_keys_exception

logging.basicConfig(filename='keyboard_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# 설정 파일 경로
CONFIG_FILE = 'config.json'
class State:
    def __init__(self):
        self.monitoring = False
        self.collected_keys = []
        self.chatingchang = False
        self.toggle_key = None
        self.start_key = ['enter', '\\']
        self.init_start_key = ['enter', '\\']
        self.end_key = '\\'
        self.forprint_toggle= '\\'
        self.forprint_start= 'enter'
        self.forprint_end= None

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            logging.warning(f"설정 파일 '{CONFIG_FILE}'가 존재하지 않습니다. ")
            return
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # read start_key
                temp_start_key = config.get('start_key', self.start_key[0])
                if temp_start_key in start_keys_exception:
                    logging.warning(f"{temp_start_key}는 사용할 수 없는 키입니다.")
                    temp_start_key = self.start_key[0]
                # read start_key_2
                temp_start_key2 = config.get('start_key_2', self.start_key[1])
                if temp_start_key2 in start_keys_exception:
                    logging.warning(f"{temp_start_key2}는 사용할 수 없는 키입니다.")
                    temp_start_key2 = self.start_key[1]
                self.start_key = [temp_start_key, temp_start_key2]
                self.forprint_start = temp_start_key + "," + temp_start_key2
                # read end_key
                temp_end_key = config.get('end_key', self.end_key)
                if temp_end_key in end_keys_exception:
                    logging.warning(f"{temp_end_key}는 사용할 수 없는 키입니다.")
                    temp_end_key = self.end_key
                self.end_key = temp_end_key
                self.forprint_end = temp_end_key
                # read toggle key
                if self.end_key in self.start_key:
                    self.toggle_key = self.end_key
                    self.forprint_toggle = self.end_key
                    self.forprint_end = None
                    self.end_key = None
                    if self.end_key == self.start_key[0]: 
                        self.start_key[0] = None
                        self.forprint_start = self.start_key[1]
                    else: 
                        self.start_key[1] = None
                        self.forprint_start = self.start_key[0]
        except Exception as e:
            logging.error(f"설정 파일 로드 중 오류 발생: {e}")
            print(f"설정 파일 로드 중 오류 발생: {e}")
        logging.info(f"프로그램 실행: start key:{self.start_key}, end key:{self.end_key}, toggle key:{self.toggle_key}")