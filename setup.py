#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

dependencies = ['requests>=2.25.1', 'dataclasses>=0.6', 'dataclasses-json>=0.5.4', 'marshmallow>=3.12.2']

setuptools.setup(
    name="servicestack",
    version="0.0.4",
    author="ServiceStack, Inc.",
    author_email="team@servicestack.net",
    description="ServiceStack Python Service Clients",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ServiceStack/servicestack-python",
    license="BSD-3-Clause",
    keywords='servicestack,client,dotnet',
    install_requires=dependencies,
    packages=setuptools.find_packages(),
    tests_require=['pytest', 'dataclasses>=0.6', 'dataclasses-json>=0.5.4', 'requests>=2.25.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    py_modules=["servicestack"],
    python_requires='>=3.9',
)
