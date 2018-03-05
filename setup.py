#!/usr/bin/env python
import os
import re
import glob

from setuptools import setup
from setuptools import find_packages
import versioneer


packages = find_packages("src", exclude=['docs'])

package_data = {
    'networkmanager_wireless_web_config': ["static/**"],
}

setup(
    name='nm-wireless-web-config',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='NetworkManager Hotpot Config',
    author='xingci.xu',
    author_email='x007007007@hotmail.com',
    url='https://github.com/x007007007/',
    package_data=package_data,
    install_requires=[
    ],
    dependency_links=[],
    package_dir={
        '': "src",
    },  # yapf:disable
    packages=packages,
    entry_points={
        'console_scripts': [
            'nm-wireless-config-monitor=networkmanager_wireless_web_config.monitor:main'  # yapf:disable
        ]
    },
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7"
    ]
)
