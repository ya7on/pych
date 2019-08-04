"""Setup py2ch application."""

from os.path import dirname, join

from setuptools import setup

version = '1.0'

setup(
    name='pych',
    author='BehindLoader',
    version=version,
    packages=['pych'],
    license='MIT',
    description='Python 2ch API client.',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    install_requires=['requests==2.22.0'],
)
