import os
import logging
import sys

logger = logging.getLogger(__name__)


class CommandExecutor:
    @staticmethod
    def lock_screen():
        os.system("gnome-screensaver-command -l")

    @staticmethod
    def is_screen_unlocked():
        return os.system("gnome-screensaver-command -q | grep \"is active\"") != 0

    @staticmethod
    def check_if_apt_package_installed(package_name: str):
        status = os.system(f"dpkg -s {package_name} | grep \"ok installed\"")
        return True if status == 0 else False

    @staticmethod
    def check_required_packages():
        with open("apt_packages.txt") as packages_file:
            packages_list = packages_file.read().split("\n")
            for package in packages_list:
                is_installed = CommandExecutor.check_if_apt_package_installed(package)
                if not is_installed:
                    logger.debug(f"Please install package \"{package}\" from your terminal.")
                    print(f"Please install package \"{package}\" from your terminal.")
                    sys.exit()


