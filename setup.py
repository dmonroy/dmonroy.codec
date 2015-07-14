#!/usr/bin/env python
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTestCommand(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='dmonroy.codec',
    version='0.1.2',
    author='Darwin Monroy',
    author_email='contact@darwinmonroy.com',
    packages=['dmonroy.codec'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    tests_require=[
        'pytest'
    ],
    cmdclass = {
        'test': PyTestCommand
    },
    description='Data encoding and decoding schemas',
)