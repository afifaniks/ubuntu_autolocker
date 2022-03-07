import time
from abc import ABC, abstractmethod


class IListener(ABC):
    def __init__(self, max_inactivity_time: int):
        self.last_activity_time = time.time()
        self.max_inactivity_time = max_inactivity_time

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def update_activity_time(self):
        self.last_activity_time = time.time()

    def is_active(self):
        if (time.time() - self.last_activity_time) < self.max_inactivity_time:
            return True
        else:
            return False
