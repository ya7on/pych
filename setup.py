"""Setup py2ch application."""

from os.path import dirname, join

from setuptools import setup

version = '1.0'

setup(
    name='py2ch',
    author='BehindLoader',
    version=version,
    packages=['py2ch'],
    license='MIT',
    description='Python 2ch API client.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=['requests==2.22.0'],
)
