# Distutils script for python3-xlib-trunk

from distutils.core import setup
import Xlib

setup(
    name='python3-xlib-trunk',
    version=Xlib.__version_string__,

    description='Python 3 X Library',
    url='https://github.com/guoci/python3-xlib-trunk',
    license='GPL',

    author='Peter Liljenberg',
    author_email='petli@ctrl-c.liu.se',
    maintainer = 'Guoci',
    maintainer_email = 'guociz@gmail.com',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
    ],
    packages=[
        'Xlib',
        'Xlib.ext',
        'Xlib.keysymdef',
        'Xlib.protocol',
        'Xlib.support',
        'Xlib.xobject'
    ],
    long_description = '''
    A Python 3 port of the development version of python-xlib.
    ''',
)

