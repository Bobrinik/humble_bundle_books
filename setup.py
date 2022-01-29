#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as readme_file:
    readme = readme_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="humble-get",
    author_email='bobrinik@pm.me',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    description="Humble-gs all of your books from Humblebundle order.",
    entry_points={
        'console_scripts': [
            'humble_get=humble_get.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='humble_get',
    name='humble_get',
    packages=find_packages(include=['humble_get']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bobrinik/humble_get',
    version='0.1.0',
    zip_safe=False,
)
