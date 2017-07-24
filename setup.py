"""Installer for the asyncio-getting-started package."""

from setuptools import find_packages
from setuptools import setup


setup(
    name='asyncio-getting-started',
    version='0.1',
    description='.',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'License :: Other/Proprietary License',
    ],
    author='Gasper Karantan Vozel',
    author_email='karantan@gmail.com',
    url='http://github.com/karantan/asyncio-getting-started',
    keywords='asyncio',
    license='MIT License',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
    ],
)
