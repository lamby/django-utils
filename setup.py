"""
setup.py file for building fool components.

Nothing in this file should need to be edited, please see accompanying
package.json file if you need to adjust metadata about this package.

Borrowed almost wholesale from Armstrong http://armstrongcms.org/
"""

from setuptools import setup, find_packages

version = '0.0.6.2.dev0'

install_requires = ['pytest', 'django-model-utils >= 2.0.2', 'requests', ]

setup_kwargs = {
    "name": "fool-django-utils",
    "description": "django-utils with more Foolishness added",
    "author": "The Motley Fool",
    "author_email": "github@fool.com",
    "url": "https://github.com/themotleyfool/django-utils.git",
    "packages": find_packages(),
    "include_package_data": True,
    "install_requires": install_requires,
    "version": version,
    "dependency_links": ['http://localshop.foolhq.com/packages/',],
    "classifiers": [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    "setup_requires": [
        'setuptools-git'
    ]
}

setup(**setup_kwargs)