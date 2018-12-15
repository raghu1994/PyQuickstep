#!/usr/bin/env python
import io
from setuptools import setup, find_packages

version = "1.0.6"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PyQuickstep",
    version=version,
    url='https://github.com/raghu1994/PyQuickstep',
    description='Pure Python Quickstep Driver',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'cryptography', 'google', 'protobuf', 'grpcio', 'grpcio-tools'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'LICENSE :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE V3 (GPLV3)',
        'Topic :: Database',
    ],
    keywords="Quickstep",
)
