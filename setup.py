#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
	'absl-py==0.10.0',
	'astor==0.8.1',
	'certifi==2020.6.20',
	'click==8.0.3',
	'colorama==0.4.4',
	'cycler==0.10.0',
	'dataclasses==0.8',
	'dlib==19.16.0',
	'Flask==2.0.2',
	'Flask-Cors==3.0.10',
	'gast==0.2.2',
	'google-pasta==0.2.0',
	'grpcio==1.32.0',
	'h5py==2.8.0',
	'importlib-metadata==2.0.0',
	'imutils==0.5.1',
	'itsdangerous==2.0.1',
	'Jinja2==3.0.3',
	'Keras==2.2.4',
	'Keras-Applications==1.0.8',
	'Keras-Preprocessing==1.1.2',
	'kiwisolver==1.2.0',
	'Markdown==3.3',
	'MarkupSafe==2.0.1',
	'matplotlib==3.0.0',
	'numpy==1.16.0',
	'opencv-python==3.4.3.18',
	'opt-einsum==3.3.0',
	'protobuf==3.13.0',
	'pyparsing==2.4.7',
	'python-dateutil==2.8.1',
	'PyYAML==5.3.1',
	'scipy==1.1.0',
	'six==1.15.0',
	'tensorboard==1.15.0',
	'tensorflow==1.15.2',
	'tensorflow-estimator==1.15.1',
	'termcolor==1.1.0',
	'Werkzeug==2.0.2',
	'wincertstore==0.2',
	'wrapt==1.12.1',
	'zipp==3.3.0'
]

setup(
    name='Siamese_for_face_recognization',
    version='0.0.1',
    description="Models used for face_recognition by siamese neural network.",
    long_description=readme,
    long_description_content_type="text/markdown"
    author="AlphonseInbarajXavier",
    author_email='xalphonse@gmail.com',
    url='https://github.com/xalphonseinbaraj/Siamese_for_face_recognization',
    packages=[
        'Siamese_for_face_recognization',
    ],
    package_dir={'Siamese_for_face_recognization': 'Siamese_for_face_recognization'},
    package_data={
        'Siamese_for_face_recognization': ['models/*.dat'],
		'Siamese_for_face_recognization': ['models/*.xml'],
		'Siamese_for_face_recognization': ['models/*.h5'],
		
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='Siamese_for_face_recognization',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],

)
