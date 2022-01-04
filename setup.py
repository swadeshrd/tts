from setuptools import setup

setup(
    name='TTSUG',
    version='0.1.0',
    description='A Python package for converting the text to speech',
    url='https://github.com/swadeshrd/tts',
    author='Swadesh Ranjan Dash',
    author_email='swadesh5dash@gmail.com',
    license='MIT',
    packages=['tts'],
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)