from setuptools import setup, find_packages
from os import path

DIR = path.dirname(path.abspath(__file__))

DESCRIPTION = "The decentralized file sync solution for seamless and secure data transfer across devices."

AUTHORS = "Kanda-Mashiro"

EMAIL = ""

URL = "https://github.com/Kanda-Mashiro/meshsync"

with open(path.join(DIR, "requirements.txt")) as f:
    INSTALL_PACKAGES = f.read().splitlines()

with open(path.join(DIR, "README.md")) as f:
    README = f.read()

# get __version__ from _version.py
ver_file = path.join("meshsync", "_version.py")
with open(ver_file) as f:
    exec(f.read())

VERSION = __version__

setup(
    name="meshsync",
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author=AUTHORS,
    author_email=EMAIL,
    url=URL,
    license="MIT",
    packages=find_packages(),
    install_requires=INSTALL_PACKAGES,
    include_package_data=True,
    python_requires=">=3",
    keywords=["meshsync", "decentration", "file-synchronization", "multi-devices"],
    tests_require=["pytest", "pytest-cov", "pytest-sugar"],
)
