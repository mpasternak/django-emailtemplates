# -*- encoding: utf-8 -*-

import os
from setuptools import setup

setup(name = 'django-emailtemplates',
	description = 'Send e-mails using database-stored e-mail templates with Django',
        version = '0.2',
        author = u'Michał Pasternak - FHU Kagami',
        author_email = 'michal.dtz@gmail.com',
        url = 'http://fhu-kagami.pl/',
        license = 'MIT',
        packages = ['emailtemplates', 'emailtemplates.conf'],
        include_package_data = True,
        install_requires = ['django'],
        zip_safe = False)