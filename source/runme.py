import keyboard
from state import State
from logger import log_typing


class EventHandler:
    def __init__(self, state:State):
        self.state = state

        self.typing = False
        self.toggle_key = 'enter'
        self.exit_key = 'esc'
        self.color_table_key = 'end'

    def event_handler(self, event):
        if event.event_type == 'up': return True
        return self.process(event.name)
    
    @log_typing
    def process(self, event):
        """command process"""
        if event == self.toggle_key:
            self.typing = not self.typing
            self.state.clear()
            return True
        elif event == self.exit_key:
            self.typing = False
            self.state.clear()
            return True
        
        if not self.typing: return True
        """typing process"""
        result = self.state.record(event)
        self.state.write()
        return result

def main():
    state = State()
    e = EventHandler(state)

    keyboard.hook(e.event_handler, suppress=True)
    keyboard.wait()

if __name__ == "__main__":
    main()