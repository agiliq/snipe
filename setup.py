#!/usr/bin/python

from setuptools import setup

setup(name = "Snipe",
    version = '0.1',
    scripts= ['snipe/bin/snipe'],
    py_modules = ['snipe'],
    description = "Minimal screenshot app",
    author = "Agiliq Solutions",
    author_email = "hello@agiliq.com",
    license = "BSD",
    url = "https://github.com/agiliq/snipe",
    long_description = """Minimal screenshot app"""
)
