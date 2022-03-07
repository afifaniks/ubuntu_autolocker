
# Ubuntu Autolocker

Your friendly bot that may save your Ubuntu Desktop from intrusion when you forgot to lock the screen!


## What it does?

The bot keeps track of your keyboard and mouse activity. And when it finds you're inactive for a given (Yes you decide the period) number of time, it looks for you through the camera (Yes, it's a bit intelligent too ;]) and if you're not there, it **LOCKS** your screen! 


## Pre-requisites
`gnome-screensaver` needs to be installed. if it's not there, install it by -

```
sudo apt install gnome-screensaver
```
Install required packages by-
```
pip install -r requirements.txt
```
And kaboom!
## How to run?

Navigate to `main.py`. It looks like -
```
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
```
Here you basically configure two things!

`MAX_TIMEOUT`: The time interval you want the program to check for activity.

`IMAGE_PATH`: Your image (By default there is my image, you should replace it by yours). This image will be used by the system to look for you when there is no keyboard or mouse activity within the `MAX_TIMEOUT` interval.
## Acknowledgements

 - [face_recognition](https://github.com/ageitgey/face_recognition)