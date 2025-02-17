import keyboard
from key_map import shift_keys
from utils import start_typing, end_typing, exit_typing
from state import State

def on_key_press(event, state:State):
    """command key process"""
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
    
    """typing key process"""
    if event.name in state.engkor_key:
        state.chmod()
        return
    event_len = len(event.name)
    if event.name == 'backspace':
        state.backspace()
    elif event.name == 'space':
        state.space()
    elif event_len == 1:
        state.insert(event.name)

def main():
    state = State()
    keyboard.on_press(lambda event: on_key_press(event, state))
    state.init_print()
    state.overlay.mainloop()

if __name__ == "__main__":
    main()