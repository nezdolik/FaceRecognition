from distutils.core import setup


install_requires = [
    'boost',
    'boost-python --with-python3',
    'dlib',
    'pipe'
    ]

setup(
    name='FaceRecognition',
    version='0.0.1',
    packages=[''],
    url='',
    license='',
    author='nezdolik',
    author_email='nezdolik@spotify.com',
    description='',
    install_requires=install_requires
)


