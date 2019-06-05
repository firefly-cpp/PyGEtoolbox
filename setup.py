# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import sys

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PyGEtoolbox',
    version='0.0.1',
    description='Gene expression toolbox in Python',
    long_description=readme,
    author='firefly-cpp',
    url='https://github.com/firefly-cpp/PyGEtoolbox',
    license=license,
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development'
      ],
    include_package_data=True,
    packages=find_packages(exclude=('tests', 'docs'))
)
