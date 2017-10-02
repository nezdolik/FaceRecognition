import sys
import dlib
import cv2

from pipe import Pipe

from steps import common

@Pipe
def project_faces(detect_face_landmarks):
    pose_landmarks, image = detect_face_landmarks()