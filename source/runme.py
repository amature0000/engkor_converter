import keyboard
from overlay import OverlayWindow
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox
import utils
import sys

class Controller(QObject):
    openOverlay = pyqtSignal()
    closeOverlay = pyqtSignal(bool)
    processOverlay = pyqtSignal()
    settingsSignal = pyqtSignal()

    def __init__(self, overlay: OverlayWindow):
        super().__init__()
        self.openOverlay.connect(overlay.show_message)
        self.closeOverlay.connect(overlay.exit_message)
        self.processOverlay.connect(overlay.process_message)
        self.settingsSignal.connect(overlay.change_settings)

        self.typing = False

    def on_key_press(self, key):
        if key == 'esc' and self.typing:
            self.typing = False
            self.closeOverlay.emit(True)
            return
        if key == '\\' and self.typing:
                self.closeOverlay.emit(False)
        if key == 'home':
            self.settingsSignal.emit()
        if key == 'enter':
            self.typing = not self.typing
            if self.typing: 
                self.openOverlay.emit()
            else:
                self.processOverlay.emit()

def main():
    app = QApplication(sys.argv)

    # rect = (-1, -1, 2561, 1441)
    rect = utils.get_window_rect()  # 실제 윈도우 크기 가져올 때 사용
    hud_size = utils.read_json()

    overlay = OverlayWindow(hud_size, rect)
    overlay.textSubmitted.connect(utils.process_and_insert)

    controller = Controller(overlay)
    keyboard.on_release(lambda e: controller.on_key_press(e.name))
    app.aboutToQuit.connect(keyboard.unhook_all)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()