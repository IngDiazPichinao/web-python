#!/usr/bin/env python3
""" CNS Timber Industry Web based Interfaces.
"""
from setuptools import setup, find_packages

constants = {
    'name'               : 'cns-web-sav',
    'long_description'   : __doc__,
    'version'            : '0.0.1.dev2014061200',
    'packages'           : find_packages('src'),
    'package_dir'        : {'': 'src'},
    'namespace_packages' : [
        'cns',
        'cns.web'
    ],

    'install_requires'   : [
        'cns-orm     >= 0.1.0.dev2015101000',
        'cns-orm-sav >= 0.0.1.dev2014051500',
        'SQLAlchemy  >= 0.9.8',
        'psycopg2    == 2.5.4',
        'Flask       >= 0.10.1'
    ],

    'entry_points'       : {
        'console_scripts': [
            'cns-web-sav = cns.web.sav.main:main'
        ]
    },

    'dependency_links'     : [],
    'include_package_data' : True,
    'zip_safe'             : False
}

setup(**constants)
