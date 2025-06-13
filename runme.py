from pynput import keyboard
from overlay import OverlayWindow
from state import State

def on_key_press(key, overlay: OverlayWindow):
    if key == keyboard.Key.esc:
        overlay.hide_message()
        return
    if key == keyboard.Key.enter:
        overlay.show_message()

def main():
    state = State()
    overlay = OverlayWindow(state.offset_x, state.offset_y, state.hud_size, state.process_and_insert)
    listener = keyboard.Listener(on_press=lambda key:on_key_press(key, overlay))
    listener.start()
    overlay.mainloop()

if __name__ == "__main__":
    main()