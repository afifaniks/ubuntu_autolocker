import time
from threading import Thread

from service.keyboard_listener import KeyboardListener
from service.mouse_listener import MouseListener

if __name__ == "__main__":
    kb = KeyboardListener(max_inactivity_time=5)
    ms = MouseListener(max_inactivity_time=5)
    thread = Thread(target=kb.start)
    thread2 = Thread(target=ms.start)
    thread.start()
    thread2.start()

    while True:
        time.sleep(2)
        print(f"Keyboard Active: {kb.is_active()}")
        print(f"Mouse Active: {ms.is_active()}")

