from setuptools import find_packages, setup

setup(
    name='bbox-tools',
    packages=find_packages(include=['bbox-tools']),
    version='0.1.0',
    description=
    "This is a library that allows reading and converting bounding box annotations in different formats and then exporting the data in various popular formats like 'voc', 'coco', 'yolo'. It can handle diverse bbox typs like (CWH, TLBR, TLWH) and allows converting them like a breeze.",
    author='Olivier D\'Ancona',
    license='GPL-3.0',
    install_requires=['pandas', 'xmltodict'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)