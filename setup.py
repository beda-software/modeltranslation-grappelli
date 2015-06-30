# -*- coding: utf-8 -*-
from setuptools import setup


README = open('README.md').read()


setup(
    name='modeltranslation-grappelli',
    version='0.0.1',
    author='Konstantin Liuterovich',
    author_email='constantin3627@gmail.com',

    description='django-modeltranslation with support grappelli.',
    long_description=README,
    url='https://github.com/Brogency/modeltranslation-grappelli',
    license='BSD',

    packages=[
        'modeltranslation_grappelli',
        'modeltranslation_grappelli.admin',
    ],
    package_data={
        'modeltranslation_grappelli': ['static/modeltranslation-grappelli/css/*.css',
                                       'static/modeltranslation-grappelli/js/*.js']},
    install_requires=[
        'django-modeltranslation==0.7.3',
    ],

    zip_safe=False,
    include_package_data=True
)