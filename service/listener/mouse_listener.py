import logging

from pynput.mouse import Listener

from service.listener.ilistener import IListener

logger = logging.getLogger(__name__)


class MouseListener(IListener):
    def __init__(self, max_inactivity_time: int):
        super().__init__(max_inactivity_time=max_inactivity_time)
        self.listener: Listener = None

    def on_move(self, x, y):
        self.update_activity_time()

    def on_click(self, x, y, button, pressed):
        self.update_activity_time()

    def on_scroll(self, x, y, dx, dy):
        self.update_activity_time()

    def start(self):
        self.listener = Listener(
                on_click=self.on_click,
                on_scroll=self.on_scroll,
                on_move=self.on_move)
        self.listener.start()
        logger.debug("Mouse listener started...")
        self.listener.join()

    def stop(self):
        self.listener.stop()
