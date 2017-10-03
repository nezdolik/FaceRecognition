import sys
import dlib
import cv2
import openface

from pipe import Pipe

from common import *

ALIGNED_IMAGE_DIM = 300

@Pipe
def project_faces(data):
    faces, image = data
    face_aligner = openface.AlignDlib(PREDICTOR_MODEL)

    for i, face_rect in enumerate(faces):
        # Use openface to calculate and perform the face alignment
        alignedFace = face_aligner.align(ALIGNED_IMAGE_DIM, image, face_rect, landmarkIndices=openface.AlignDlib.INNER_EYES_AND_BOTTOM_LIP)
        # Save the aligned image to a file
        cv2.imwrite("aligned_data/aligned_face_{}.jpg".format(i), alignedFace)

    return faces, image

