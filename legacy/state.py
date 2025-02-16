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
        self.first_type = False
        self.collected_keys = []
        self.chatingchang = False
        self.toggle_key = '\\'
        self.start_key = ['enter', None]
        self.end_key = None
        self.forprint_toggle= '\\'
        self.forprint_start= 'enter'
        self.forprint_end= None
        self.additional_backspace = 0
        self.play_sound=True
        self.fast_forward= True

    def init_print(self):
        print("https://github.com/amature0000/engkor_converter\n")
        if self.forprint_start:
            print(f"시작 키: '{self.forprint_start}'")
        if self.forprint_end:
            print(f"출력 키: '{self.forprint_end}'")
        if self.forprint_toggle:
            print(f"토글 키: '{self.forprint_toggle}'")
        print(f"초기화 키: 'esc'")
        print("종료하려면 창을 닫거나 Ctrl + C를 누르세요.")
        print()

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            logging.warning(f"설정 파일 '{CONFIG_FILE}'가 존재하지 않습니다. ")
        else: 
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # read start_key
                    temp_start_key = config.get('start_key', self.start_key[0])
                    if temp_start_key in start_keys_exception:
                        logging.warning(f"start_key, {temp_start_key}는 사용할 수 없는 키입니다.")
                        temp_start_key = self.start_key[0]
                    # read start_key_2
                    temp_start_key2 = config.get('start_key_2', self.start_key[1])
                    if temp_start_key2 in start_keys_exception:
                        logging.warning(f"start_key_2, {temp_start_key2}는 사용할 수 없는 키입니다.")
                        temp_start_key2 = self.start_key[1]
                    self.start_key = [temp_start_key, temp_start_key2]
                    self.forprint_start = temp_start_key + "," + temp_start_key2
                    # read end_key
                    temp_end_key = config.get('end_key', self.end_key)
                    if temp_end_key in end_keys_exception:
                        logging.warning(f"end_key, {temp_end_key}는 사용할 수 없는 키입니다.")
                        temp_end_key = self.end_key
                    self.end_key = temp_end_key
                    self.forprint_end = temp_end_key
                    self.forprint_toggle = None
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
                    # read play_sound
                    self.play_sound = config.get('play_sound', self.end_key)
                    if self.play_sound != True and self.play_sound != False:
                        logging.warning(f"play_sound, {self.play_sound}는 잘못된 인자입니다.")
                        self.play_sound = True
                    # read fast_foward
                    self.fast_forward = config.get('experimental_fastforward', self.fast_forward)
                    if self.fast_forward != True and self.fast_forward != False:
                        logging.warning(f"experimental_fastfoward, {self.fast_forward}는 잘못된 인자입니다.")
                        self.play_sound = True
            except Exception as e:
                logging.error(f"설정 파일 로드 중 오류 발생: {e}")
        logging.info(f"프로그램 실행: start key:{self.start_key}, end key:{self.end_key}, toggle key:{self.toggle_key}, play sound:{self.play_sound}, fastforward:{self.fast_forward}")