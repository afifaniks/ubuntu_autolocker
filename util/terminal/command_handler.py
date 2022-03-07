import os


class CommandHandler:
    @staticmethod
    def lock_screen():
        os.system("gnome-screensaver-command -l")
