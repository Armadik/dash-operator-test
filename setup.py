from sys import version_info

from setuptools import find_packages, setup

if version_info[:2] < (3,8):
    raise RuntimeError(
        'Unsupported python version %s.' % '.'.join(version_info)
    )


_NAME = 'dashoper'
setup(
    name=_NAME,
    version='0.0.1',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
    author='Armadik',
    include_package_data=True,
    install_requires=[
        'kubernetes==18.20.0',
    ],
    entry_points={
        'console_scripts': [
            '{0} = {0}.cli:main'.format(_NAME),
        ]
    }
)