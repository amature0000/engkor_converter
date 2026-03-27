import keyboard
from state import State
from logger import Logger, log_typing
from time import sleep

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
    
    def _change_delay(self):
        self.state.change_delay()
        return self.typing


def main():
    state = State()
    e = EventHandler(state)
    Logger.delay = state.delay
    Logger.log()

    keyboard.on_press(e.process, suppress=True)
    keyboard.wait()

if __name__ == "__main__":
    main()