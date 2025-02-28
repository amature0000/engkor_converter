from keyboard import on_press
from state import State

def on_key_press(event, state:State):
    """command process"""
    if event.name == state.start_key:
        state.typing = not state.typing
        if state.typing: state.start_typing()
        else: state.exit_typing()
        return
    elif event.name == state.end_key:
        state.end_typing()
        return
    elif event.name == state.exit_key:
        state.exit_typing()
        return
    if not state.typing:
        return
    
    """typing process"""
    if event.name in state.engkor_key:
        # 유저 편의성을 위해 채팅창이 켜져 있는 동안만 한/영 동작
        state.chmod()
        return
    event_len = len(event.name)
    if event.name == 'backspace':
        state.backspace()
    elif event.name == 'space':
        state.insert(' ')
    elif event_len == 1:
        state.insert(event.name)

def main():
    state = State()
    on_press(lambda event: on_key_press(event, state))
    state.overlay.mainloop()

if __name__ == "__main__":
    main()