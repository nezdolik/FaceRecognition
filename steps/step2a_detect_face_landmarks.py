import sys
import dlib
from pipe import Pipe
from skimage import io

from steps import common

@Pipe
def detect_landmarks(find_faces):
    image, faces = find_faces()
    face_pose_predictor = dlib.shape_predictor(common.PREDICTOR_MODEL)

    win = dlib.image_window()

    for i, face_rect in enumerate(faces):
        print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(),
                                                                                 face_rect.right(), face_rect.bottom()))

        # Draw a box around each face we found
        win.add_overlay(face_rect)

        # Get the the face's pose
        pose_landmarks = face_pose_predictor(image, face_rect)

        # Draw the face landmarks on the screen.
        win.add_overlay(pose_landmarks)

    dlib.hit_enter_to_continue()

    return pose_landmarks, image


