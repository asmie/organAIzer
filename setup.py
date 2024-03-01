# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='organAIzer',
    version='0.1.0',
    description='Personal organizing tool with AI support',
    long_description=readme,
    author='Piotr Olszewski',
    author_email='asmie@asmie.pl',
    url='https://github.com/asmie/organAIzer',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)