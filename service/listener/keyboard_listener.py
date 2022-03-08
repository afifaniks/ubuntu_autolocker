import logging

from pynput.keyboard import Listener

from service.listener.ilistener import IListener

logger = logging.getLogger(__name__)

class KeyboardListener(IListener):
    def __init__(self, max_inactivity_time: int):
        super().__init__(max_inactivity_time=max_inactivity_time)
        self.listener: Listener = None

    def on_press(self, key):
        self.update_activity_time()

    def on_release(self, key):
        self.update_activity_time()
        if key == "stop":
            return False

    def start(self):
        self.listener = Listener(
                on_press=self.on_press,
                on_release=self.on_release)
        self.listener.start()
        logger.debug("Keyboard listener started...")
        self.listener.join()

    def stop(self):
        self.listener.stop()
