#!/usr/bin/env python

import os
import setuptools


setuptools.setup(
  name='remoteconfig',
  version='0.2.4',

  author='Max Zheng',
  author_email='maxzheng.os @t gmail.com',

  description='A simple wrapper for localconfig that allows for reading config from a remote server',
  long_description=open('README.rst').read(),

  url='https://github.com/maxzheng/remoteconfig',

  install_requires=[
    'localconfig>=0.4',
    'requests',
  ],

  license='MIT',

  package_dir={'': 'src'},
  packages=setuptools.find_packages('src'),
  include_package_data=True,

  setup_requires=['setuptools-git'],

  classifiers=[
    'Development Status :: 5 - Production/Stable',

    'Intended Audience :: Developers',
    'Topic :: Software Development',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
  ],

  keywords='configuration remote http config',
)
