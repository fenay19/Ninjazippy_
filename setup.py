from setuptools import setup, find_packages

setup(
    name="NinjaZipPy",
    version="0.1.0",
    description="Simple Python utility to create and extract .7z archives",
    author="Your Name",
    packages=find_packages(),
    install_requires=["py7zr>=0.18"],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "ninjazippy=ninjazippy.cli:main",
        ]
    },
)
