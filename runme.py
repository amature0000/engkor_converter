from pynput import keyboard
from overlay import OverlayWindow
from state import State
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
import sys

class Controller(QObject):
    openOverlay = pyqtSignal()
    closeOverlay = pyqtSignal()

    def __init__(self, overlay: OverlayWindow):
        super().__init__()
        self.openOverlay.connect(overlay.show_message)
        self.closeOverlay.connect(overlay.hide_message)

    def on_key_press(self, key):
        if key == keyboard.Key.esc:
            self.closeOverlay.emit()
            return
        if key == keyboard.Key.enter:
            self.openOverlay.emit()

def main():
    app = QApplication(sys.argv)
    state = State()
    overlay = OverlayWindow(state.offset_x, state.offset_y, state.hud_size)
    controller = Controller(overlay)
    listener = keyboard.Listener(on_press=lambda key:controller.on_key_press(key))
    listener.start()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()