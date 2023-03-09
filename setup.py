import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    version="1.0",
    name="audio_whisper",
    packages=find_packages(),
    py_modules=["audio_whisper"],
    author="Danilo Dominguez",
    install_requires=[
        'python-multipart',
        'fastapi[all]',
        'uvicorn[standard]',
        'whisper @ git+https://github.com/openai/whisper.git@main#egg=whisper'
    ],
    description="Generate transcripts for audio files",
    # entry_points={
        # 'console_scripts': ['yt_whisper=yt_whisper.cli:main'],
    # },
    include_package_data=True,
)