#!/usr/bin/env python
# coding: utf-8

# http://stackoverflow.com/a/10975371/554319
import os
import io
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test


# https://packaging.python.org/guides/single-sourcing-package-version/
version = {}
with open(os.path.join("src", "poliastro", "__init__.py")) as fp:
    exec(fp.read(), version)


# https://docs.pytest.org/en/latest/goodpractices.html#manual-integration
class PyTest(test):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        import pytest

        sys.exit(pytest.main(shlex.split(self.pytest_args)))

# http://blog.ionelmc.ro/2014/05/25/python-packaging/
setup(
    name="poliastro",
    version=version['__version__'],
    description="Python package for Orbital Mechanics",
    author="Juan Luis Cano",
    author_email="hello@juanlu.space",
    url="http://poliastro.github.io/",
    download_url="https://github.com/poliastro/poliastro",
    license="MIT",
    keywords=[
        "aero", "aerospace", "engineering",
        "astrodynamics", "orbits", "kepler", "orbital mechanics"
    ],
    python_requires=">=3.5",
    install_requires=[
        "numpy",
        "astropy>=1.2,!=2.0.0",
        "matplotlib",
        "jplephem",
        "scipy",
        "beautifulsoup4",
        "requests",
        "pandas",
        "numba>=0.25",
    ],
    tests_require=[
        "coverage",
        "pytest-cov",
    ],
    extras_require={
        'dev': [
            "pep8",
            "mypy",
            "sphinx",
            "sphinx_rtd_theme",
            "nbsphinx",
            "ipython"
        ]
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'poliastro = poliastro.cli:main'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    long_description=io.open('README.rst', encoding='utf-8').read(),
    package_data={"poliastro": ['tests/*.py']},
    include_package_data=True,
    zip_safe=False,
    cmdclass={'test': PyTest},
)
