"""
This script is used to package and distribute a Python package. It provides metadata about the package such as its name, version, dependencies, and entry points.
"""

from setuptools import setup, find_packages

setup(
    name="pyconsole",
    version="0.1",
    author="sikandar",
    author_email="sikandar1838@gmail.com",
    description="A simple console utility for printing messages with color using colorama",
    long_description="A Python package providing a utility for printing messages with color to the console.",
    long_description_content_type="text/markdown",
    url="https://github.com/sikandar1838/pyconsole",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["colorama"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
