#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import json
import os
import sys

try:
    from setuptools import find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages
    from distutils.extension import Extension

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

try:
    from Cython.Build import cythonize
    use_cython = True
except ImportError:
    use_cython = False

from pkg_resources import parse_requirements, RequirementParseError

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('LICENSE') as f:
    license_str = f.read()

try:
    with open('requirements.txt') as f:
        ireqs = parse_requirements(f.read())
except RequirementParseError:
    raise
requirements = [str(req) for req in ireqs]


def convert_to_filename_format(name):
    name = name.replace(".", "/")
    return name+"/"

def define_extensions(use_cython=True):
    src_ext = '*.pyx' if use_cython else '*.cpp'
    modules = [Extension("histomicstk." + name,
                         [os.path.join("histomicstk", convert_to_filename_format(name) + src_ext)],
                         language='c++')
               for name in ['features', 'segmentation.label', 'segmentation.nuclear']]
    if use_cython:
        return cythonize(modules)
    else:
        return modules

setup(name='histomicstk',
      long_description=readme + '\n\n' + history,
      author='Kitware, Inc.',
      author_email='developers@digitalslidearchive.net',
      url='https://github.com/DigitalSlideArchive/HistomicsTK',
      packages=find_packages(exclude=['doc']),
      package_dir={'histomicstk':
                   'histomicstk'},
      include_package_data=True,
      install_requires=requirements,
      license=license_str,
      zip_safe=False,
      keywords='histomicstk',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      test_suite='plugin_tests',
      setup_requires=["Cython>=0.24"],
      ext_modules=define_extensions(use_cython)
)
