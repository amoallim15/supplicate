import sys
import os
from setuptools import find_packages, setup

# version info --= read without importing
_locals = {}
exec(open("src/_version.py").read(), None, _locals)
version = _locals["__version__"]

install_requires = open("requirements.txt").read().strip().split("\n")
dev_requires = open("requirements.dev.txt").read().strip("\n")
long_description = open("README.md").read()

setup(
    name="Supplicate",
    version=version,
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={"console_scripts": ["supp = cli.program:main"]},
    python_requires=">=3.6",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amoallim15/supplicate",
    license="MIT License",
    author="Ali Moallim",
    author_email="amoallim15@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
)
