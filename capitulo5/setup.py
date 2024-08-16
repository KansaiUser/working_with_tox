from setuptools import setup, find_packages
from pathlib import Path

# Read the version from the VERSION file
with open(Path(__file__).resolve().parent / "regmod" / "VERSION") as version_file:
    version = version_file.read().strip()

setup(
    name='regmod',
    version=version,
    packages=find_packages(),
    include_package_data=True,  # Ensure non-code files are included
)
