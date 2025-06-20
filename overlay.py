from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QFont
import utils

class OverlayWindow(QWidget):
    textSubmitted = pyqtSignal(str)

    def __init__(self, hud_size: float, rect:tuple):
        super().__init__(flags=Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Window)
        self.setAttribute(Qt.WA_ShowWithoutActivating, False)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 인스턴스 필드
        self.typing = False
        self.ignore_enter = 0
        # geometry 계산
        offset_x = -22.90 * hud_size + 99.93
        offset_y = -12.50 * hud_size + 99.775

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
        self.input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(self.input)

    def show_message(self):
        """
        입력창을 보여주고 포커스 설정
        """
        if self.typing: return
        self.typing = True
        self.input.clear()
        self.show()
        utils.simulate_key_process("alt") # 포커스 뺏어오기
        self.input.activateWindow()

    def exit_message(self):
        """
        창 닫기
        """
        if not self.typing: return
        self.input.clear()
        self.hide()
        self.typing = False
        utils.simulate_key_process('esc') # esc 키 전달

    def process_message(self):
        """
        입력된 텍스트 전달 후 창 닫기
        """
        text = self.input.text()
        
        self.input.clear()
        self.hide()
        self.typing = False
        if not text: 
            utils.simulate_key_process('esc') # esc 키 전달
            return
        self.textSubmitted.emit(text) # 텍스트 전달