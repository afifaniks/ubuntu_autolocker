import logging

import face_recognition
import numpy as np

logger = logging.getLogger(__name__)


class FaceRecognizer:
    def __init__(self, known_image: np.ndarray):
        self.known_encoding = face_recognition.face_encodings(known_image)[0]

    def is_matched(self, unknown_image: np.ndarray) -> bool:
        try:
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces([self.known_encoding], unknown_encoding)
            return results[0]
        except Exception as e:
            logger.debug(f"Exception occurred while matching face. {e}")
            return False

