from state import State
import time
import keyboard

def start_typing(state:State):
    state.typing = True
    state.clear(True)
    state.init_print()
    print('한글화 모니터링 시작')

def end_typing(state:State):
    if not state.typing: return
    process_and_insert(state)
    state.typing = False
    state.clear()
    print('한글화 모니터링 종료')

def exit_typing(state:State):
    state.typing = False
    state.clear()
    state.init_print()

def process_and_insert(state:State):
    state.eng_to_kor(True)
    try:
        # 기존 입력 삭제
        keyboard.press('esc')
        time.sleep(0.05)
        keyboard.release('esc')
        keyboard.press('enter')
        time.sleep(0.05)
        keyboard.release('enter')
        # 한글 문자열 타이핑
        if len(state.fixed_keys) > 0:
            time.sleep(0.1)
            keyboard.write(state.fixed_keys, delay=0.01)
        print(f'문장 입력 완료: {state.fixed_keys}')
        # 텍스트 전송
        keyboard.press('enter')
        time.sleep(0.05)
        keyboard.release('enter')
    except Exception as e:
        print(f"입력 처리 중 오류 발생: {e}")
