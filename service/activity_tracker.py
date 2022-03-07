import logging
from threading import Thread

from service.face_recognition.face_recognizer import FaceRecognizer
from service.io.ilistener import IListener
from util.camera.webcam_util import CameraUtil
from util.terminal.command_handler import CommandHandler

logger = logging.getLogger(__name__)


class ActivityTracker:
    def __init__(self,
                 keyboard_listener: IListener,
                 mouse_listener: IListener,
                 face_recognizer: FaceRecognizer):
        self.keyboard_listener: IListener = keyboard_listener
        self.mouse_listener: IListener = mouse_listener
        self.keyboard_listener_thread: Thread = Thread(target=self.keyboard_listener.start)
        self.mouse_listener_thread: Thread = Thread(target=self.mouse_listener.start)
        self.face_recognizer: FaceRecognizer = face_recognizer

    def monitor(self):
        self.keyboard_listener_thread.start()
        self.mouse_listener_thread.start()

    def is_user_active(self) -> bool:
        is_peripherals_active: bool = self.mouse_listener.is_active() or \
            self.keyboard_listener.is_active()

        logger.debug(f"Peripherals Activity Status: {is_peripherals_active}")
        if not is_peripherals_active and CommandHandler.is_screen_unlocked():
            logger.debug(f"Screen Unlocked Status: {CommandHandler.is_screen_unlocked()}")
            try:
                face_match = self.face_recognizer.is_matched(CameraUtil.capture_photo())
                logger.debug(f"Face Match: {face_match}")
                if face_match:
                    return True
                else:
                    logger.debug(f"No Face Matched")
                    return False

            except Exception as e:
                logger.debug(f"Exception occurred while matching face {e}")
                return False

        return is_peripherals_active
