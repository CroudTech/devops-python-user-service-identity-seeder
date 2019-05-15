#!/usr/bin/env python
# -- coding: utf-8 --
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    print("setup tools required. Please run: "
          "pip install setuptools).")
    sys.exit(1)

setup(name='seed_identities',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='Reads users from user service and posts / updates identity server via rest api',
      author='Jim Robinson',
      author_email='jscrobinson@gmail,com',
      license='Apache2.0',
      packages=['seed_identities'],
      install_requires=[
            "click==7.0",
            "GitPython>=2.1.11",
            "oyaml>=0.8",
            "coloredlogs>=9.0",
            "semver>=2.8.1",
            "requests>=2.20.1",
      ],
      entry_points=''' #for click integration
          [console_scripts]
          seed_identities=seed_identities.cli:cli
      '''
      )
