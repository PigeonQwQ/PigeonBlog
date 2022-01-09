import codecs
import os
import re
from typing import List

import setuptools


def read(*paths: str) -> str:
    """
    Reading file as str using codecs.open()
    :param paths: file path
    :return: file content as string
    """
    path = os.path.join(os.path.dirname(__file__), *paths)
    with codecs.open(path) as f:
        return f.read()


def find_version(*paths: str) -> str:
    """
    Fetch package version from file
    :param paths: the file contains version field
    :return: version string(semver)
    """
    version_file = read(*paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to locate version string.")


def parse_requirement(*paths) -> List[str]:
    requirement_file = read(*paths)
    return requirement_file.splitlines()


setuptools.setup(
    name="pigeon-blog",
    version=find_version("pigeon", "blog", "__init__.py"),
    description="A lite blog system, 咕咕咕",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url="https://darc.pro/",
    author="DarcJC",
    license="MIT",
    packages=setuptools.find_packages(exclude=('tests.*', 'tests')),
    include_package_data=True,
    install_requires=parse_requirement("requirements.txt"),
    python_requires=">=3.10",
    entry_points={
        'console_scripts': ['pigeon-admin=pigeon.blog.cli:main'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
)
