import codecs
import os

import pyxboxapi

from distutils.core import setup

b = os.path.abspath(os.path.dirname(__file__))


def read(f):
    return codecs.open(os.path.join(b, f), 'r').read()

setup(
    name='pyxboxapi',
    version=pyxboxapi.__version__,
    url='https://github.com/teeebs/pyxboxapi',
    download_url='https://github.com/teeebs/pyxboxapi/tarball/%s' % pyxboxapi.__version__,
    license='MIT License',
    author='Trevor Veralrud',
    author_email="trevor.veralrud@gmail.com",
    install_requires=['requests'],
    description='Wrapper for unofficial Xbox API (https://xboxapi.com)',
    packages=['pyxboxapi'],
    package_data={'': ['README.md', 'LICENSE']},
    include_package_data=True,
    platforms='any',
    keywords=["xbox", "api"],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Games/Entertainment',
        ],
)