import tkinter
import exec_once
import tkinter.font as tkfont
from pynput.keyboard import Controller, Key

# ratio
#WIDTH_R = 18.75 #470
#HEIGHT_R = 3.9 #50

class OverlayWindow:
    def __init__(self, offset_x, offset_y, hud_size, callback):
        self.process_text = callback
        self.isopen = False
        # Tkinter 설정
        self.root = tkinter.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        # self.root.configure(bg="lightgray")
        # self.root.attributes("-transparentcolor", "white")
        self.font = tkfont.Font(family="d2coding", size=16, weight='bold')
        self.inputbox = tkinter.Entry(
            self.root,
            font=self.font,
            bg="white",
            fg="black",
            relief="flat",
            insertbackground="black"
        )
        self.inputbox.pack(fill="both", expand=True, padx=5, pady=5)

        rect = (-1, -1, 2561, 1441)
        # rect = exec_once.get_window_rect() # causes polling
        left, top, right, bottom = rect
        # 채팅창 크기 계산
        overlay_x = int((right - left) * offset_x / 100)
        overlay_y = int((bottom - top) * offset_y / 100)
        width = int((right - left) * 18.75 / 100 * hud_size / 0.9)
        height = int((bottom - top) * 3.9 / 100 * hud_size / 0.9)

        self.root.geometry(f"{width}x{height}+{overlay_x}+{overlay_y}")
        self.root.withdraw()
        # ===================================
        self.root.update_idletasks()
        self.label_width = self.root.winfo_width() - 10
        # ===================================
        self.inputbox.bind("<Return>", self._handle_submit)

    def show_message(self, placeholder=""):
        if self.isopen: return
        self.isopen = True
        self.inputbox.delete(0, "end")
        self.inputbox.insert(0, placeholder)
        # inputbox 열고 포커스 설정. 사용자 입력 받기
        self.root.deiconify()
        self.inputbox.focus_set()
        self.inputbox.focus_force()

    def hide_message(self):
        self.root.withdraw()
        self.isopen = False

    def _handle_submit(self, _event):
        self.root.withdraw()
        text = self.inputbox.get()
        self.process_text(text)
        self.isopen = False # withdraw는 즉시, 플래그 설정은 process_text 다음에 해야 함.

    def mainloop(self):
        self.root.mainloop()