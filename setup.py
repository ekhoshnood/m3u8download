#!/usr/bin/env python
# coding=utf-8

"""
python distribute file
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

from setuptools import find_packages, setup


def requirements_file_to_list(fn="requirements.txt"):
    """read a requirements file and create a list that can be used in setup.

    """
    with open(fn, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


setup(
    name="m3u8download",
    version=1.0,
    packages=find_packages(exclude=("utils",)),
    install_requires=requirements_file_to_list(),
    entry_points={
        'console_scripts': [
            'downloadm3u8 = m3u8download.main:main',
        ]
    },
    package_data={
        'm3u8download': ['logger.conf']
    },
    author="ebrahim khoshnood",
    author_email="khoshnood966@gmail.com",
    maintainer="ebrahim khoshnood",
    maintainer_email="khoshnood966@gmail.com",
    description="a cli program to download video at m3u8 url",
    long_description=open('README.md').read(),
    long_description_content_type='text/x-md',
    license="GPLv2+",
    url="https://pypi.org/project/m3u8download/",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 3.5',
    ]
)
