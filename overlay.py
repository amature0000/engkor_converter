import tkinter
import exec_once
import tkinter.font as tkfont

# ratio
#WIDTH_R = 18.75 #470
#HEIGHT_R = 3.9 #50

class OverlayWindow:
    def __init__(self, offset_x, offset_y, hud_size):
        # Tkinter 설정
        self.root = tkinter.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        # self.root.configure(bg="lightgray")
        # self.root.attributes("-transparentcolor", "white")
        self.font = tkfont.Font(family="d2coding", size=16, weight='bold')
        self.label = tkinter.Label(
            self.root, 
            text="", 
            font=self.font, 
            bg="lightgray", 
            fg="black",
            anchor='w')
        self.label.pack(fill="both", expand=True, padx=5, pady=5)

        #rect = (-1, -1, 2561, 1441)
        rect = exec_once.get_window_rect() # causes polling
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

    def show_message(self, message):
        while self.font.measure(message) + 5 >= self.label_width:
            message = message[1:]
        self.label.config(text=message)
        self.root.deiconify()  # 창 보이기

    def mainloop(self):
        self.root.mainloop()