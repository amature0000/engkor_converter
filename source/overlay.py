import tkinter as tk
import tkinter.font as tkFont
import utils

# ratio
WIDTH_R = 18.75 #470
HEIGHT_R = 3.9 #50

class OverlayWindow:
    def __init__(self):
        # Tkinter 설정
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.font = tkFont.Font(family="d2coding", size=16, weight='bold')
        self.label = tk.Label(
            self.root, 
            text="", 
            font=self.font, 
            bg="lightgray", 
            fg="black",
            anchor='w')
        self.label.pack(fill="both", expand=True, padx=5, pady=5)
        # ===================================
        self.resize()
        self.root.withdraw()
    
    def resize(self):
        # rect = (-1, -1, 2561, 1441)
        rect = utils.get_window_rect()
        hud_size = utils.read_json()
        # logistic regression
        offset_x = -22.90 * hud_size + 99.93
        offset_y = -12.50 * hud_size + 99.78

        left, top, right, bottom = rect

        overlay_x = int((right - left) * offset_x / 100)
        overlay_y = int((bottom - top) * offset_y / 100)
        width = int((right - left) * WIDTH_R / 100 * hud_size / 0.9)
        height = int((bottom - top) * HEIGHT_R / 100 * hud_size / 0.9)

        self.root.geometry(f"{width}x{height}+{overlay_x}+{overlay_y}")

        self.root.update_idletasks()
        self.label_width = self.root.winfo_width() - 10

    def show_message(self, message):
        while self.font.measure(message) + 5 >= self.label_width:
            message = message[1:]
        self.label.config(text=message)
        self.root.deiconify()  # 창 보이기

    def mainloop(self):
        self.root.mainloop()