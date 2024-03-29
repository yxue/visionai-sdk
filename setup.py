"""Set up the package"""
from os import path

from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="useful-lva-sdk",
    version="0.1.7",
    description="Unofficial Vision AI Live Video Analytics SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yan Xue",
    author_email="xueyan.sjtu@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "google-api-core",
        "google-auth",
        "googleapis-common-protos",
        "graphviz",
        "grpcio",
        "protobuf",
    ]
)
