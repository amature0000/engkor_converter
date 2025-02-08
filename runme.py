import keyboard
from key_map import shift_keys
from utils import start_typing, end_typing, exit_typing
from state import State

def on_key_press(event, state:State):
    if event.name == state.start_key:
        state.typing = not state.typing
        if state.typing: start_typing(state)
        else: exit_typing(state)
        return
    elif event.name == state.end_key:
        end_typing(state)
        return
    elif event.name == state.exit_key:
        exit_typing(state)
        return
    if not state.typing:
        return
    if event.name in state.engkor_key:
        state.mode = not state.mode
        state.put()
        return
    """typing이 켜져 있는 동안 키를 눌렀을 때 실행되는 로직"""
    event_len = len(event.name)
    if event.name == 'backspace':
        state.backspace()
    elif event.name == 'space':
        state.put(' ')
    elif event_len == 1:
        state.insert(event.name)
        """
        key = event.name.lower()
        if event.name.lower() in shift_keys: key = event.name
        state.insert(key)
        """
    state.show_overlay()

def main():
    state = State()
    keyboard.on_press(lambda event: on_key_press(event, state))
    state.init_print()
    state.overlay.mainloop()

if __name__ == "__main__":
    main()