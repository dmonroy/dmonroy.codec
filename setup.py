#!/usr/bin/env python
from setuptools import setup
import tests

setup(
    name='dmonroy.codec',
    version='0.0.0',
    author='Darwin Monroy',
    author_email='contact@darwinmonroy.com',
    packages=['dmonroy.codec'],
    include_package_data=True,
    install_requires=[],
    tests_require=[
        'pytest'
    ],
    cmdclass = {
        'test': tests.PyTestCommand
    },
    description='Data encoding and decoding schemas',
)
