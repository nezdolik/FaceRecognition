import pipe

from step1_find_faces import find_faces
from step2a_detect_face_landmarks import  detect_landmarks
from step2b_project_faces import project_faces

result = find_faces | detect_landmarks | project_faces