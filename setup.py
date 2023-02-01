from setuptools import find_packages, setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bboxtools',
    packages=find_packages(include=['bboxtools']),
    version='0.1.0',
    description="Converting bounding box annotations to popular formats like a breeze.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ODAncona/bbox-tools",
    author='Olivier D\'Ancona',
    license='GPL-3.0',
    install_requires=['pandas', 'xmltodict'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)