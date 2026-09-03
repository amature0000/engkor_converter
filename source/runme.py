import keyboard
from state import State, EK_KEYS
from logger import Logger, log_typing

class EventHandler:
    def __init__(self, state:State):
        self.state = state

        self.typing = False
        self.command = { # controls self.typing
            'enter': lambda: not self.typing,
            'esc': lambda: False,
            'end': self._change_delay
        }

    @log_typing
    def process(self, event):
        name = event.name
        """command process"""
        if name in self.command:
            self.typing = self.command[name]()
            self.state.clear()
            return True
        
        if not self.typing: return True
        """typing process"""
        result = self.state.process(name)
        return result

    def release_callback(self, event):
        name = event.name
        if self.typing:
            if name in EK_KEYS: return False
            if self.state.mode: return False
        return True
    
    def _change_delay(self):
        self.state.change_delay()
        return self.typing


def main():
    state = State()
    e = EventHandler(state)
    Logger.delay = state.delay
    Logger.log()

    keyboard.on_press(e.process, suppress=True)
    keyboard.on_release(e.release_callback, suppress=True)
    keyboard.wait()

if __name__ == "__main__":
    main()