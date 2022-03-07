import time

from service.activity_tracker import ActivityTracker
from service.io.keyboard_listener import KeyboardListener
from service.io.mouse_listener import MouseListener

if __name__ == "__main__":
    MAX_TIMEOUT: int = 5
    kb = KeyboardListener(max_inactivity_time=MAX_TIMEOUT)
    ms = MouseListener(max_inactivity_time=MAX_TIMEOUT)

    activity_checker: ActivityTracker = ActivityTracker(kb, ms)
    activity_checker.monitor()

    while True:
        time.sleep(2)
        print(activity_checker.is_user_active())