import keyboard
from state import State
import utils
from overlay import OverlayWindow
class EventHandler:
    def __init__(self, overlay:OverlayWindow, state:State):
        self.overlay = overlay
        self.state = state

        self.typing = False
        self.start_key = 'enter'
        self.end_key = '\\'
        self.exit_key = 'esc'

    def on_key_press(self, event):
        if not self.overlay.root.winfo_exists():
            keyboard.unhook_all()
            exit()
        """command process"""
        if event == self.start_key:
            self.typing = not self.typing
            self.state.clear()
        elif event == self.end_key and self.typing:
            utils.process_and_insert(self.state.extract())
            self.typing = False
            self.state.clear()
        elif event == self.exit_key:
            self.typing = False
            self.state.clear()
        if not self.typing:
            self.overlay.root.withdraw()
            return
        
        """typing process"""
        self.state.record(event)
        self.overlay.show_message(self.state.process())

def main():
    rect = (-1, -1, 2561, 1441)
    # rect = utils.get_window_rect()
    hud_size = utils.read_json()

    overlay = OverlayWindow(hud_size, rect)
    state = State()

    e = EventHandler(overlay, state)
    keyboard.on_press(lambda event: e.on_key_press(event.name))

    overlay.mainloop()

if __name__ == "__main__":
    main()