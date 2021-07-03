#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

dependencies = ['dataclasses-json>=0.5.4','requests>=2.25.1']

setuptools.setup(
    name="servicestack",
    version="0.0.1",
    author="ServiceStack, Inc.",
    author_email="team@servicestack.net",
    description="ServiceStack Python Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ServiceStack/servicestack-python",
    license="BSD-3-Clause",
    keywords='servicestack,client,dotnet',
    install_requires=dependencies,
    packages=setuptools.find_packages(),
    tests_require=['pytest','dataclasses-json>=0.5.4','requests>=2.25.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    py_modules=["servicestack"],
    python_requires='>=3.8',
)
