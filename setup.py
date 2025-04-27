from setuptools import setup, find_packages
import os

setup(
    name = "ptap",
    version = "v1.2",
    packages = find_packages(include = ["ptap", "ptap.*"]),
    install_requires = [
        "requests",
        "pyperclip",
    ],
    entry_points = {
        "console_scripts": [
            "ptap=ptap.main:main",
        ],
    },
    author = "Far3k",
    author_email = "far3000yt@gmail.com",
    description = "The best tool to generate AI prompts from code projects and make any AI understand a whole project!",
    long_description = open("README.md", encoding="utf-8").read() if os.path.exists("README.md") else "",    long_description_content_type = "text/markdown",
    url = "https://github.com/Far3000-YT/PTAP",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.7",
    license = "MIT",
)