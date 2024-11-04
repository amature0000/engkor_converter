import keyboard
import sys
import time
from key_map import shift_keys
from utils import end_monitoring, exit_monitoring, start_monitoring, toggle_monitoring
import state
import logging

def on_key_press(event):
    if event.name == 'enter':
        state.chatingchang = not state.chatingchang  
        if not state.chatingchang:
            exit_monitoring()
            return

    if event.name == 'esc':
        exit_monitoring()
        return
    elif event.name == state.toggle_key:
        toggle_monitoring()
        return
    elif event.name == state.start_key:
        start_monitoring()
        return
    elif event.name == state.end_key:
        end_monitoring()
        return
        
    if not state.monitoring:
        return
        
    logging.info(f"키 입력 감지: {event.name}")
        
    if event.name == 'backspace' and len(state.collected_keys) > 0:
        state.collected_keys.pop()
    elif event.name == 'space' or len(event.name) == 1:
        print(event.name)
        key = ' ' if event.name == 'space' else event.name.lower()
        if event.name.lower() in shift_keys:
            key = event.name
        state.collected_keys.append(key)

def main():
    state.load_config()
    keyboard.on_press(on_key_press)
    if state.toggle_key:
        print(f"프로그램이 실행 중입니다. '{state.toggle_key}' 키를 눌러 입력을 시작/종료하세요.")
    else:
        print(f"프로그램이 실행 중입니다. '{state.start_key}'/'{state.end_key}' 키를 눌러 입력을 시작/종료하세요.")
    print("config.json을 수정하여 변경 가능합니다.")
    print("종료하려면 Ctrl + C를 누르세요.")
    print()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
        sys.exit()

if __name__ == "__main__":
    main()
