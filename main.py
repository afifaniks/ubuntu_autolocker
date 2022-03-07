import logging
import time

from service.activity_tracker import ActivityTracker
from service.face_recognition.face_recognizer import FaceRecognizer
from service.io.keyboard_listener import KeyboardListener
from service.io.mouse_listener import MouseListener
from util.image.image_util import ImageUtil
from util.terminal.command_handler import CommandHandler

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    MAX_TIMEOUT: int = 10
    kb = KeyboardListener(max_inactivity_time=MAX_TIMEOUT)
    ms = MouseListener(max_inactivity_time=MAX_TIMEOUT)
    fr = FaceRecognizer(known_image=ImageUtil.read_image("you/image.jpeg"))

    activity_checker: ActivityTracker = ActivityTracker(kb, ms, fr)
    activity_checker.monitor()

    while True:
        user_active: bool = activity_checker.is_user_active()
        if not user_active:
            CommandHandler.lock_screen()
        time.sleep(5)
