import keyboard
from state import State

def on_key_press(event, state: State):
    if not state.overlay.root.winfo_exists():
        keyboard.unhook_all()
        exit()
    """command process"""
    if event.name == state.start_key:
        state.typing = not state.typing
        state.clear(state.typing)
        return
    elif event.name == state.end_key:
        if not state.typing: return
        state.process_and_insert()
        state.typing = False
        state.clear()
        return
    elif event.name == state.exit_key:
        state.typing = False
        state.clear()
        return
    if not state.typing:
        return
    
    """typing process"""
    if event.name in state.engkor_key:
        # 유저 편의성을 위해 채팅창이 켜져 있는 동안만 한/영 동작
        state.mode = not state.mode
        state.show_overlay()
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
    keyboard.on_press(lambda event: on_key_press(event, state))
    state.overlay.mainloop()

if __name__ == "__main__":
    main()