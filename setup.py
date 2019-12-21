"""
Created: 4/22/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
import os
from pathlib import Path
import sys
from setuptools import setup, find_packages


# Borrowed heavily from Django and Requests
# https://github.com/django/django/blob/master/setup.py
# https://github.com/kennethreitz/requests/blob/master/setup.py


def read(*file):
    with open(os.path.join(os.path.dirname(__file__), *file)) as f:
        return f.read()


CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of WrapPlotLib requires Python {}.{}, but you're trying to
install it on Python {}.{}.
""".format(*REQUIRED_PYTHON, *CURRENT_PYTHON))
    sys.exit(1)

HERE = Path(__file__).parent

about = {}
exec(read('wrapplotlib', '__version__.py'), about)

setup(
    author=about['__author__'],
    author_email=about['__author_email__'],
    classifiers=[
        "License :: OSI Approved :: Apache License 2.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    description=about['__description__'],
    install_requires=[
        'matplotlib>=3.1.2',
        'pandas>=0.25.3',
        'sejings'
    ],
    license=about['__licence__'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    name=about['__name__'],
    packages=find_packages(),
    project_urls={
        'Source': 'https://github.com/EmilianoJordan/WrapPlotLib/',
        'Tracker': 'https://github.com/EmilianoJordan/WrapPlotLib/issues',
    },
    tests_require=[
        'pytest>=3.10.0',
        'click>=7.0'
    ],
    url=about['__url__'],
    version=about['__version__'],
)
