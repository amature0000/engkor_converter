import logging
from state import State
import time
import keyboard
from eng_kor_converter import engkor

def toggle_monitoring(state:State):
    state.monitoring = not state.monitoring
    if state.monitoring or len(state.collected_keys) == 0:
        logging.info("키보드 입력 모니터링 시작")
        print("키보드 입력 모니터링 시작")
        state.monitoring = True
    else:
        logging.info("키보드 입력 모니터링 중지")
        print("키보드 입력 모니터링 중지")
        process_and_insert(state)
    state.collected_keys.clear()

def start_monitoring(state:State):
    logging.info("키보드 입력 모니터링 시작")
    print("키보드 입력 모니터링 시작")
    state.monitoring = True
    state.collected_keys.clear()

def end_monitoring(state:State):
    if not state.monitoring:
        logging.warning("모니터링 상태가 아닙니다.")
        return
    
    state.monitoring = False
    process_and_insert(state)
    state.collected_keys.clear()

def exit_monitoring(state:State):
    state.monitoring = False
    logging.info("모니터링 취소")
    print("모니터링 취소")
    state.collected_keys.clear()
    state.chatingchang = False

def process_and_insert(state:State):
    try:
        time.sleep(0.1)
        # 수집된 키를 한글 문자열로 변환
        english_str = ''.join(state.collected_keys)
        korean_string = engkor(english_str)
        logging.info(f"수집된 한글 입력: {korean_string}")
        print(f"수집된 한글 입력: {korean_string}")

        if korean_string:
            # 영어 입력 삭제
            for _ in range(len(state.collected_keys) + state.additional_backspace):
                press_once('backspace')
            logging.info(f"백스페이스 실행 : {len(state.collected_keys) + state.additional_backspace}회")
            state.additional_backspace = 0
            # 한글 문자열 타이핑
            keyboard.write(korean_string, delay=0.01)
            logging.info("한글 문자열 타이핑 완료")
        else:
            logging.warning("변환할 한글 문자가 없습니다.")
            print("변환할 한글 문자가 없습니다.")
        time.sleep(0.1)
    except Exception as e:
        logging.error(f"입력 처리 중 오류 발생: {e}")

def press_once(str):
    time.sleep(0.01)
    keyboard.press_and_release(str)