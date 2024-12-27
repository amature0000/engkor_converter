import winsound as ws
from state import State
import threading

def beep_async(freq, dur):
    ws.Beep(freq, dur)

def activate(state:State):
    if state.play_sound == False: return
    activate_thread = threading.Thread(target=beep_async, args=(200, 25))
    activate_thread.start()

def deactivate(state:State):
    if state.play_sound == False: return
    activate_thread = threading.Thread(target=beep_async, args=(100, 25))
    activate_thread.start()