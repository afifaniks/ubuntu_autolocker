from threading import Thread

from service.io.ilistener import IListener


class ActivityTracker:
    def __init__(self, keyboard_listener: IListener, mouse_listener: IListener):
        self.keyboard_listener: IListener = keyboard_listener
        self.mouse_listener: IListener = mouse_listener
        self.keyboard_listener_thread: Thread = Thread(target=self.keyboard_listener.start)
        self.mouse_listener_thread: Thread = Thread(target=self.mouse_listener.start)

    def monitor(self):
        self.keyboard_listener_thread.start()
        self.mouse_listener_thread.start()

    def is_user_active(self):
        return self.mouse_listener.is_active() or \
            self.keyboard_listener.is_active()
