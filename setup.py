#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="sentry-dingding-feelys",
    version='0.0.4',
    author='lcfevr',
    author_email='lcfevr@163.com',
    url=' https://github.com/lcfevr/sentry-dingding.git',
    description='A Sentry extension which send errors stats to DingDing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='sentry dingding feelys',
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
            'sentry_dingding_feelys = sentry_dingding_feelys.plugin:DingDingPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
    ]
)
