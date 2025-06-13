from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from pynput.mouse import Controller as MouseController, Button

class OverlayWindow(QWidget):
    textSubmitted = pyqtSignal(str)

    def __init__(self, offset_x: float, offset_y: float, hud_size: float):
        super().__init__(flags=Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Window)
        self.setAttribute(Qt.WA_ShowWithoutActivating, False)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # geometry 계산
        rect = (-1, -1, 2561, 1441)
        # rect = exec_once.get_window_rect()  # 실제 윈도우 크기 가져올 때 사용
        left, top, right, bottom = rect
        overlay_x = int((right - left) * offset_x / 100)
        overlay_y = int((bottom - top) * offset_y / 100)
        width = int((right - left) * 18.75 / 100 * hud_size / 0.9)
        height = int((bottom - top) * 3.9 / 100 * hud_size / 0.9)
        self.setGeometry(overlay_x, overlay_y, width, height)

        # UI 구성
        font = QFont("D2Coding", 16, QFont.Bold)
        self.input = QLineEdit(self)
        self.input.setFont(font)
        self.input.setPlaceholderText("")
        self.input.setFocusPolicy(Qt.StrongFocus)
        

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(self.input)

    def show_message(self):
        """
        입력창을 보여주고 포커스 설정
        """
        self.show()
        self.input.show()
        self.input.setFocus()
        self.input.activateWindow()

    def hide_message(self):
        """
        입력된 텍스트를 print()한 뒤 입력창 숨김
        """
        self.input.releaseKeyboard()
        text = self.input.text()
        print(text)
        self.input.clear()
        self.hide()