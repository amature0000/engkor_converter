import keyboard
from overlay import OverlayWindow
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
import utils
import sys


class Controller(QObject):
    openOverlay = pyqtSignal()
    closeOverlay = pyqtSignal()

    def __init__(self, overlay: OverlayWindow):
        super().__init__()
        self.openOverlay.connect(overlay.show_message)
        self.closeOverlay.connect(overlay.exit_message)

    def on_key_press(self, key):
        if key == 'esc':
            self.closeOverlay.emit()
            return
        if key == 'enter':
            self.openOverlay.emit()    

def main():
    app = QApplication(sys.argv)

    # rect = (-1, -1, 2561, 1441)
    rect = utils.get_window_rect()  # 실제 윈도우 크기 가져올 때 사용

    hud_size, offset_x, offset_y = utils.read_process_json()
    overlay = OverlayWindow(offset_x, offset_y, hud_size, rect)
    
    controller = Controller(overlay)
    overlay.textSubmitted.connect(utils.process_and_insert)

    keyboard.on_press(lambda e: controller.on_key_press(e.name))
    app.aboutToQuit.connect(keyboard.unhook_all)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
