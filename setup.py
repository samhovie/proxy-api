"""REST python package configuration."""

from setuptools import setup

setup(
    name='REST_Example',
    version='0.1.0',
    packages=['REST_Example'],
    include_package_data=True,
    install_requires=[
        'flask',
        'arrow',
        'sh',
    ],
)