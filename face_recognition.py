import pipe

from steps.step1_find_faces import find_faces
from steps.step2a_detect_face_landmarks import  detect_landmarks

result = find_faces | detect_landmarks