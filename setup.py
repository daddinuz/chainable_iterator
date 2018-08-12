import sys

import setuptools

major, minor1, minor2, release, serial = sys.version_info

if major < 3 and minor1 < 5:
    raise ValueError('Python3.5 or greater is required')

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

if __name__ == '__main__':
    setuptools.setup(
        name='chainable_iterator',
        version='0.1.0',
        description='',
        long_description=readme,
        author='daddinuz',
        author_email='daddinuz@gmail.com',
        url='https://github.com/daddinuz/chainable_iterator',
        license=license,
        packages=setuptools.find_packages(exclude=('examples', 'tests')),
    )
