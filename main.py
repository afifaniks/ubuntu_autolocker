import logging
import time

from service.tracker.activity_tracker import ActivityTracker
from service.face_recognition.face_recognizer import FaceRecognizer
from service.listener.keyboard_listener import KeyboardListener
from service.listener.mouse_listener import MouseListener
from util.image.image_util import ImageUtil
from util.terminal.command_executor import CommandExecutor

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    CommandExecutor.check_required_packages()

    MAX_TIMEOUT: int = 10
    IMAGE_PATH: str = "you/image.jpeg"

    kb_listener: KeyboardListener = KeyboardListener(max_inactivity_time=MAX_TIMEOUT)
    mouse_listener: MouseListener = MouseListener(max_inactivity_time=MAX_TIMEOUT)
    face_recognizer: FaceRecognizer = FaceRecognizer(known_image=ImageUtil.read_image(IMAGE_PATH))

    activity_checker: ActivityTracker = ActivityTracker(kb_listener, mouse_listener, face_recognizer)
    activity_checker.monitor()

    while True:
        user_active: bool = activity_checker.is_user_active()
        if not user_active:
            CommandExecutor.lock_screen()
        time.sleep(MAX_TIMEOUT)
