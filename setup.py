#!/usr/bin/env python
from setuptools import setup, find_packages

from sentry_dingtalk import VERSION, NAME

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author='ansheng',
    author_email='ianshengme@gmail.com',
    url='https://github.com/anshengme/sentry-dingtalk',
    description='A Sentry extension which send errors stats to DingTalk',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry dingtalk',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sentry_dingtalk = sentry_dingtalk.plugin:DingTalkPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "License :: OSI Approved :: MIT License",
    ]
)
