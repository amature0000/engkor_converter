import keyboard
from state import State
from logger import Logger, log_typing


class EventHandler:
    def __init__(self, state:State):
        self.state = state

        self.typing = False
        self.toggle_key = 'enter'
        self.exit_key = 'esc'
        self.color_table_key = 'end'

    @log_typing
    def process(self, event):
        name = event.name
        """command process"""
        if name == self.toggle_key:
            self.typing = not self.typing
            self.state.clear()
            return True
        elif name == self.exit_key:
            self.typing = False
            self.state.clear()
            return True
        
        if not self.typing: return True
        """typing process"""
        result = self.state.process(name)
        return result

def main():
    Logger.log()

    state = State()
    e = EventHandler(state)

    keyboard.on_press(e.process, suppress=True)
    keyboard.wait()

if __name__ == "__main__":
    main()