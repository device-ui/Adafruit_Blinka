#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="Adafruit-Blinka",
    version="8.47.0",
    description="CircuitPython APIs for non-CircuitPython versions of Python such as CPython on Linux and MicroPython.",
    author="Adafruit Industries",
    author_email="circuitpython@adafruit.com",
    python_requires=">=3.7.0",
    url="https://github.com/adafruit/Adafruit_Blinka",
    package_dir={"": "src"},
    packages=find_packages("src"),
    # py_modules lists top-level single file packages to include.
    # find_packages only finds packages in directories with __init__.py files.
    py_modules=[
        "analogio",
        "bitbangio",
        "board",
        "busio",
        "digitalio",
        "keypad",
        "neopixel_write",
        "onewireio",
        "pulseio",
        "pwmio",
        "rainbowio",
        "usb_hid",
    ],

    install_requires=[
        "Adafruit-PlatformDetect>=3.70.1",
        "Adafruit-PureIO>=1.1.7",
    ],
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: MicroPython",
    ],
)
