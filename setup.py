#!/usr/bin/env python

from setuptools import setup, find_packages
import version

setup(
    name = "archmage",
    fullname = "arCHMage",
    version=version.getVersion(),
    description = "CHM decompressor",
    maintainer = "Basil Shubin",
    maintainer_email = "bashu@users.sourceforge.net",
    author = "Eugeny Korekin",
    author_email = "az@ftc.ru",
    url = "archmage.sf.net",
    license = "GPLv2+",
    keywords = ["chm", "HTML Help", "Compiled HTML", "Compressed HTML"],
    long_description = "arCHMage is a reader and decompressor for CHM format",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['archmage = archmod.cli:main'],
    },
    package_data={
        'archmod': ['*.conf', 'templates/*.html', 'templates/*.css',
                    'templates/icons/*.gif'],
    }
)
