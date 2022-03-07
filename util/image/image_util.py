from PIL import Image
import numpy as np


class ImageUtil:
    @staticmethod
    def read_image(image_path: str) -> np.ndarray:
        try:
            image = Image.open(image_path)
            image_converted = image.convert("RGB")
            return np.array(image_converted)
        except Exception as e:
            print("Error occurred while reading image")


