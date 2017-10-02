from distutils.core import setup
import distutils.command.install_data

#todo write command for model download
# class InstallModel(distutils.command.install_data):
#     def run(self):


install_requires = [
    'boost',
    'boost-python --with-python3',
    'dlib',
    'pipe', 'cv2'
    ]

dependency_links = [
    'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2'
]



setup(
    name='FaceRecognition',
    version='0.0.1',
    packages=[''],
    url='',
    license='',
    author='nezdolik',
    author_email='kateryna.nezdolii@gmail.com',
    description='',
    install_requires=install_requires
)


