# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from erlyvideo import get_version


setup(
    name='django-erlyvideo',
    version=get_version().replace(' ', '-'),
    description=u'Erlyvideo',
    license="BSD License",
    author='Aleksandr Zorin (plazix)',
    author_email='plazix@gmail.com',
    url='https://github.com/plazix/django-erlyvideo',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
