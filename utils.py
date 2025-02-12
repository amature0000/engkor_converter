from state import State
import time
import keyboard
import os

def start_typing(state:State):
    os.system('cls')
    state.init_print()
    state.typing = True
    state.fixed_keys.clear()
    state.korean_keys.clear()
    state.show_overlay()
    print('한글화 모니터링 시작')

def end_typing(state:State):
    if not state.typing: return
    state.collapse_kor_keys()
    process_and_insert(state)
    state.typing = False
    state.fixed_keys.clear()
    state.korean_keys.clear()
    state.hide_overlay()
    print('한글화 모니터링 종료')

def exit_typing(state:State):
    state.typing = False
    state.fixed_keys.clear()
    state.korean_keys.clear()
    state.hide_overlay()
    os.system('cls')
    state.init_print()

def process_and_insert(state:State):
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
            result = ''.join(state.fixed_keys)
            keyboard.write(result, delay=0.01)
        print(f'문장 입력 완료: {result}')
        keyboard.press('enter')
        time.sleep(0.05)
        keyboard.release('enter')
    except Exception as e:
        print(f"입력 처리 중 오류 발생: {e}")
