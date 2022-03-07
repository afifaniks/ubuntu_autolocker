import os
from threading import Thread

from service.face_recognition.face_recognizer import FaceRecognizer
from service.io.ilistener import IListener
from util.camera.webcam_util import CameraUtil
from util.terminal.command_handler import CommandHandler


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

        if not is_peripherals_active:
            try:
                if not self.face_recognizer.is_matched(CameraUtil.capture_photo()):
                    CommandHandler.lock_screen()
            except Exception as e:
                CommandHandler.lock_screen()

        return is_peripherals_active
