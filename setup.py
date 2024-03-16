# -*- coding: utf-8 -*-
"""Module providing setup facility."""

from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as f:
    readme = f.read()

with open('LICENSE', encoding="utf-8") as f:
    license_text = f.read()

with open('requirements.txt', encoding="utf-8") as f:
    required = f.read().splitlines()

setup(
    name='organAIzer',
    version='0.1.0',
    description='Personal organizing tool with AI support',
    long_description=readme,
    author='Piotr Olszewski',
    author_email='asmie@asmie.pl',
    url='https://github.com/asmie/organAIzer',
    license=license_text,
    entry_points={
        'console_scripts': ['oai=organAIzer.cli:cli'],
    },
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=required
)
