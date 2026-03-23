from time import sleep
import keyboard

def simulate_key_process(key):
    keyboard.press(key)
    sleep(0.05)
    keyboard.release(key)
    sleep(0.05)

def process_and_insert(text):
    simulate_key_process('esc')
    if not text: return

    # 한글 문자열 타이핑
    simulate_key_process('enter')
    keyboard.write(text, delay=0.01)
    sleep(0.01)
    simulate_key_process('enter')

def print_infos():
    print("https://github.com/amature0000/engkor_converter")
    print("EKconverter ver 3.15.3")