import keyboard
from state import State


class EventHandler:
    def __init__(self, state:State):
        self.state = state

        self.typing = False
        self.toggle_key = 'enter'
        self.exit_key = 'esc'
        self.color_table_key = 'end'

    def on_key_press(self, event):
        """command process"""
        if event == self.toggle_key:
            self.typing = not self.typing
            self.state.clear()
        elif event == self.exit_key:
            self.typing = False
            self.state.clear()
            
        if not self.typing: return
        """typing process"""
        self.state.record(event)

def main():
    state = State()

    e = EventHandler(state)
    keyboard.on_press(lambda event: e.on_key_press(event.name))

if __name__ == "__main__":
    main()