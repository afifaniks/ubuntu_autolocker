import os


class CommandHandler:
    @staticmethod
    def lock_screen():
        os.system("gnome-screensaver-command -l")

    @staticmethod
    def is_screen_unlocked():
        return os.system("gnome-screensaver-command -q | grep \"is active\"") != 0
