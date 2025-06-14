from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QFont
import ctypes
import utils

KEYEVENTF_KEYUP = 0x0002
VK_MENU = 0x12  # ALT
VK_ESCAPE = 0x1B  # ESC

def simulate_key_press(key):
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
    ctypes.windll.user32.keybd_event(key, 0, KEYEVENTF_KEYUP, 0)

class OverlayWindow(QWidget):
    textSubmitted = pyqtSignal(str)

    def __init__(self, offset_x: float, offset_y: float, hud_size: float):
        super().__init__(flags=Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Window)
        self.setAttribute(Qt.WA_ShowWithoutActivating, False)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 인스턴스 필드
        self.typing = False
        self.ignore_enter = 0
        self.ignore_esc = 0
        # geometry 계산
        # rect = (-1, -1, 2561, 1441)
        rect = utils.get_window_rect()  # 실제 윈도우 크기 가져올 때 사용

        left, top, right, bottom = rect
        overlay_x = int((right - left) * offset_x / 100)
        overlay_y = int((bottom - top) * offset_y / 100)
        width = int((right - left) * 18.75 / 100 * hud_size / 0.9)
        height = int((bottom - top) * 3.9 / 100 * hud_size / 0.9)
        self.setGeometry(overlay_x, overlay_y, width, height+10)

        font = QFont("D2Coding", 16, QFont.Bold)
        # UI 구성
        self.input = QLineEdit(self)
        self.input.setFont(font)
        self.input.setPlaceholderText("")
        self.input.setFocusPolicy(Qt.StrongFocus)
        self.input.returnPressed.connect(self.process_message)
        self.input.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(self.input)

    def setTyping(self, t):
        self.typing = t

    def show_message(self):
        """
        입력창을 보여주고 포커스 설정
        """
        if self.typing: return
        if self.ignore_enter:
            self.ignore_enter = False
            return
        self.typing = True
        self.input.clear()
        self.show()
        simulate_key_press(VK_MENU) # 포커스 뺏어오기
        self.input.activateWindow()

    def exit_message(self):
        """
        창 닫기
        """
        if not self.typing: return
        self.input.clear()
        self.hide()
        self.typing = False
        simulate_key_press(VK_ESCAPE) # esc 키 전달

    def process_message(self):
        """
        입력된 텍스트 전달 후 창 닫기
        """
        text = self.input.text()
        
        self.input.clear()
        self.hide()
        self.typing = False
        if not text: 
            simulate_key_press(VK_ESCAPE) # esc 키 전달
            return
        self.textSubmitted.emit(text) # 텍스트 전달
        self.ignore_enter = True