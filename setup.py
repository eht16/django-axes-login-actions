#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

NAME = 'django-axes-login-actions'
VERSION = '1.0.0'
DESCRIPTION = """Perform one or more actions if someone performed a login, e.g. to the admin interface."""

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=(open('README.rst', 'r').read()),
    keywords='django, security, authentication',
    author='Enrico Tröger',
    author_email='enrico.troeger@uvena.de',
    maintainer='Enrico Tröger',
    maintainer_email='enrico.troeger@uvena.de',
    url='https://github.com/eht16/django-axes-login-actions',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['django-axes'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: Log Analysis',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Security',
        'Topic :: System :: Logging',
    ],
    zip_safe=False,
)
