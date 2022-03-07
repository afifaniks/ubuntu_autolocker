import face_recognition
import numpy as np
from PIL import Image


class FaceRecognizer:
    def __init__(self, known_image: np.ndarray):
        self.known_encoding = face_recognition.face_encodings(known_image)[0]

    def is_matched(self, unknown_image: np.ndarray) -> bool:
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        return face_recognition.compare_faces([self.known_encoding], unknown_encoding)

