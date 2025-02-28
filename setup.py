from setuptools import setup, find_packages
import os

setup(
    name="PTAP",
    version="beta 0.1",
    packages=find_packages(where="ptap"),
    package_dir={"": "ptap"},
    install_requires=[
        #to complete
    ],
    entry_points={
        "console_scripts": [
            "ptap.main:main",
        ],
    },
    author="Far3000",
    author_email="far3000yt@gmail.com",
    description="The best tool to generate AI prompts from code projects and make any AI understand a whole project!",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/Far3000-YT/PTAP",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)