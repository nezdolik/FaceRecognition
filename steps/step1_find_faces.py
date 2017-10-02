import sys
import os
import dlib
from pipe import Pipe
from skimage import io


def find_faces():
    detect_faces = dlib.get_frontal_face_detector()
    win = dlib.image_window()

    if len(sys.argv) <= 1:
        raise ValueError('Please provide image name')

    image_name = sys.argv[1]

    if os.path.exists(image_name):
        print('Processing file: {}'.format(image_name))
    else:
        raise ValueError('Image {} does not exist'.format())

    image = io.imread(image_name)

    faces = detect_faces(image)

    print('Found {} faces in file {}'.format(len(faces),image_name))

    for i, face_area in enumerate(faces):
            print("Face # {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                i, face_area.left(), face_area.top(), face_area.right(), face_area.bottom()))

            win.add_overlay(face_area)

    return faces




