#!/usr/bin/env python
from setuptools import setup, find_packages

from sentry_dingtalk import VERSION

install_requires = [
    'sentry>=9.0.0',
    'requests',
]

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='sentry-dingtalk',
    version=VERSION,
    author='ansheng',
    author_email='ianshengme@gmail.com',
    url='https://github.com/anshengme/sentry-dingtalk',
    description='A Sentry extension which send errors stats to DingTalk',
    long_description=readme,
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'sentry_dingtalk = sentry_dingtalk.plugin:DingTalkPlugin'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2.7'
    ],
    keywords='sentry dingtalk',
)
