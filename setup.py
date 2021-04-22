# Copyright (c) 2021 riscLOG Solution GmbH
# See also LICENSE
"""elastic-apm integration for the Pyramid framework
"""

import os.path

from setuptools import find_packages, setup

setup(
    name='pyramid-elasticapm',
    version='1.0.1',
    install_requires=[
        'elastic-apm',
        'pyramid',
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-cache',
            'pytest-cov',
            'pytest-flake8',
            'pytest-rerunfailures',
            'pytest-sugar',
            'webtest',
            'pytest_localserver',
        ]
    },
    author='Sebastian Wehrmann (riscLOG Solution GmbH)',
    author_email='sebastian@risclog.com',
    license='BSD',
    url='https://github.com/risclog-solution/pyramid-elasticapm',
    keywords='elastic apm pyramid',
    classifiers="""\
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3 :: Only
"""[
        :-1
    ].split(
        '\n'
    ),
    description=__doc__.strip(),
    long_description=(
        '.. contents::\n\n'
        + open(os.path.join('README.rst')).read()
        + '\n\n'
        + open('CHANGES.rst').read()
    ),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
)
