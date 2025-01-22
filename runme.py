import keyboard
import sys
import time
from key_map import shift_keys
from utils import end_monitoring, exit_monitoring, start_monitoring, toggle_monitoring
from state import State
import logging

def on_key_press(event, state:State):
    if event.name == 'enter':
        state.chatingchang = not state.chatingchang  
        if not state.chatingchang:
            exit_monitoring(state)
            return
    event_len = len(event.name)
    if event.name == 'esc':
        exit_monitoring(state)
        return
    elif event.name == state.toggle_key:
        if event_len == 1:
            state.additional_backspace += 1
        toggle_monitoring(state)
        return
    elif event.name in state.start_key:
        if event_len == 1:
            state.additional_backspace += 1
        start_monitoring(state)
        if event.name == 'enter':
            state.first_type = True
        return
    elif event.name == state.end_key:
        if event_len == 1:
            state.additional_backspace += 1
        end_monitoring(state)
        return
        
    if not state.monitoring:
        return
    
    logging.info(f"키 입력 감지: {event.name}")
        
    if event.name == 'backspace' and len(state.collected_keys) > 0:
        state.collected_keys.pop()
    elif event.name == 'space' or event_len == 1:
        key = ' ' if event.name == 'space' else event.name.lower()
        if event.name.lower() in shift_keys:
            key = event.name
        state.collected_keys.append(key)

def main():
    state = State()
    state.load_config()
    keyboard.on_press(lambda event: on_key_press(event, state))
    state.init_print()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
        sys.exit()

if __name__ == "__main__":
    main()