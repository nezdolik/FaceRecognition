import sys
import dlib
from pipe import Pipe
from skimage import io

@Pipe
def detect_landmarks(find_faces):
    faces = find_faces()
    for face_area in faces:
            print("***Face # {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                1, face_area.left(), face_area.top(), face_area.right(), face_area.bottom()))