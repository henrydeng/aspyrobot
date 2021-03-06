from setuptools import setup
import re

with open('aspyrobot/__init__.py', 'r') as f:
    version = re.search(r"__version__ = '(.*)'", f.read()).group(1)

setup(
    name='aspyrobot',
    version=version,
    maintainer='Robbie Clarken',
    maintainer_email='robbie.clarken@synchrotron.org.au',
    url='https://github.com/AustralianSynchrotron/aspyrobot',
    license='MIT',
    packages=['aspyrobot'],
    install_requires=[
        'pyzmq>=15.1.0',
        'pyepics>=3.2.5rc3',
        'numpy>=1.11.0',
    ],
)
