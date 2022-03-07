import face_recognition
import numpy as np
from PIL import Image


class FaceRecognizer:
    @staticmethod
    def is_matched(known_image: np.ndarray, unknown_image: np.ndarray) -> bool:
        # known_image = face_recognition.load_image_file("biden.jpg")
        # unknown_image = face_recognition.load_image_file("unknown.jpg")

        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)

        print(results)


if __name__ == "__main__":
    im1 = Image.open("../../you/image.jpeg")
    im1 = im1.convert("RGB")
    im1 = np.array(im1)
    im2 = Image.open("../../you/img33.jpg")
    im2 = im2.convert("RGB")
    im2 = np.array(im2)

    print(FaceRecognizer.is_matched(im1, im2))
