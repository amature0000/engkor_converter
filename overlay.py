import tkinter as tk
import tkinter.font as tkFont
import win32gui
import sys
import time
import os

# Game title
GAME_TITLE = "HELLDIVERS™ 2"
# ratio
WIDTH_R = 18.75 #470
HEIGHT_R = 3.9 #50

def get_window_rect(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        print("HELLDIVERS™ 2 게임 창을 찾을 수 없습니다. 검색 중...")
        while hwnd == 0:
            print('.')
            time.sleep(1)
            hwnd = win32gui.FindWindow(None, title)
        os.system('cls')
    return win32gui.GetWindowRect(hwnd)

class OverlayWindow:
    def __init__(self, offset_x, offset_y, hud_size):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.hud_size = hud_size
        # Tkinter 창 생성 및 기본 설정
        self.root = tk.Tk()
        self.root.overrideredirect(True)              # 창 장식 제거
        self.root.attributes("-topmost", True)          # 항상 위에 표시
        #self.root.configure(bg="lightgray")
        # self.root.attributes("-transparentcolor", "white")
        self.font = tkFont.Font(family="d2coding", size=16, weight='bold')
        # 텍스트를 표시할 라벨
        self.label = tk.Label(
            self.root, 
            text="", 
            font=self.font, 
            bg="lightgray", 
            fg="black",
            anchor='w')
        self.label.pack(fill="both", expand=True, padx=5, pady=5)

        rect = get_window_rect(GAME_TITLE) # busy wait

        left, top, right, bottom = rect
        # HUD 크기 0.9 기준으로 최초 채팅창 계산
        self.overlay_x = int((right - left) * self.offset_x / 100)
        self.overlay_y = int((bottom - top) * self.offset_y / 100)
        self.width = int((right - left) * WIDTH_R / 100 * self.hud_size / 0.9)
        self.height = int((bottom - top) * HEIGHT_R / 100 * self.hud_size / 0.9)
        """
        # 오른쪽 아래를 기준으로 실제 HUD 크기를 반영하여 채팅창 재계산
        temp_x = self.overlay_x + self.width
        temp_y = self.overlay_y + self.height
        self.width = int((right - left) * WIDTH_R / 100 * self.hud_size / 0.9)
        self.height = int((bottom - top) * HEIGHT_R / 100 * self.hud_size / 0.9)
        self.overlay_x = temp_x - self.width
        self.overlay_y = temp_y - self.height
        """
        self.root.geometry(f"{self.width}x{self.height}+{self.overlay_x}+{self.overlay_y}")
        # print(f'오버레이 위치 x:{self.overlay_x}, y:{self.overlay_y}')
        self.root.withdraw()

    def show_message(self, message):
        label_width = self.root.winfo_width() - 10
        while self.font.measure(message) > label_width and len(message) > 0:
            message = message[1:]
        self.label.config(text=message)
        self.root.deiconify()  # 창 보이기

    def hide_message(self):
        self.root.withdraw()

    def mainloop(self):
        try:
            self.root.mainloop()
        except Exception:
            print("\n프로그램을 종료합니다.")
            sys.exit()
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            sys.exit()