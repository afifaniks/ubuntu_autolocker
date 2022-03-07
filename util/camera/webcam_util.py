import numpy as np
from cv2 import VideoCapture


class CameraUtil:
    @staticmethod
    def capture_photo() -> np.ndarray:
        camera = VideoCapture(0)
        _, image = camera.read()

        return image
