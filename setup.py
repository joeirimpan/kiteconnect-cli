#!/usr/bin/env python

from setuptools import setup

setup(
    name="kiteconnect-cli",
    version="0.1.0",
    description="Simple Kiteconnect CLI",
    author="Joe Paul",
    author_email="joeirimpan@gmail.com",
    packages=["kiteconnect_cli"],
    download_url="https://github.com/joeirimpan/kiteconnect-cli",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries"
    ],
    entry_points={
        'console_scripts': ['kiteconnect-cli=kiteconnect_cli.cli:cli_execute']
    },
    install_requires=['kiteconnect>=3.7.0b10', 'werkzeug'],
)
