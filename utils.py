import logging
from state import State
import time
import keyboard
from eng_kor_converter import engkor
import sound
import os

first_type = False

def toggle_monitoring(state:State):
    if state.monitoring: end_monitoring(state)
    else: start_monitoring(state)

def exit_monitoring(state:State):
    if state.monitoring == True:
        print("키보드 입력 모니터링 종료")
        sound.deactivate(state)
    logging.info("프로그램 상태 초기화")
    state.first_type = False
    state.monitoring = False
    state.chatingchang = False
    state.collected_keys.clear()
    state.additional_backspace = 0

def start_monitoring(state:State):
    if state.monitoring: return
    sound.activate(state)
    os.system('cls')
    state.init_print()
    logging.info("키보드 입력 모니터링 시작")
    print("키보드 입력 모니터링 시작")
    state.monitoring = True
    state.collected_keys.clear()

def end_monitoring(state:State):
    if not state.monitoring: return
    sound.deactivate(state)
    logging.info("키보드 입력 모니터링 종료")
    print("키보드 입력 모니터링 종료")
    process_and_insert(state)
    state.first_type = False
    state.monitoring = False
    state.collected_keys.clear()


def process_and_insert(state:State):
    try:
        # 기존 입력 삭제
        if state.first_type and state.fast_forward:
            keyboard.press('esc')
            time.sleep(0.05)
            keyboard.release('esc')
            keyboard.press('enter')
            time.sleep(0.05)
            keyboard.release('enter')
            logging.info(f"program 키 입력: esc\nprogram 키 입력: enter")
        else:
            time.sleep(0.1)
            temp = len(state.collected_keys)
            for _ in range(temp + state.additional_backspace):
                keyboard.press_and_release('backspace')
                time.sleep(0.01)
            logging.info(f"program 백스페이스 실행 : {temp + state.additional_backspace}회")
        state.additional_backspace = 0
        # 한글 문자열 타이핑
        if len(state.collected_keys) > 0:
            time.sleep(0.1)
            # 수집된 키를 한글 문자열로 변환
            english_str = ''.join(state.collected_keys)
            korean_string = engkor(english_str)
            logging.info(f"수집된 한글 입력: {korean_string}")
            print(f"수집된 한글 입력: {korean_string}")

            keyboard.write(korean_string, delay=0.01)
            logging.info("한글 문자열 타이핑 완료")
            print("한글 문자열 타이핑 완료")
    except Exception as e:
        logging.error(f"입력 처리 중 오류 발생: {e}")