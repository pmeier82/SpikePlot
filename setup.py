# -*- coding: utf-8 -*-
#
# spikeplot - setup.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-30
#

"""install script for the SpikeEval package"""
__docformat__ = 'restructuredtext'

from setuptools import setup

def find_version():
    """read version from __init__"""
    rval = '0'
    try:
        f = open('./spikeplot/__init__.py', 'r')
        try:
            for line in f:
                if line.startswith('__version__'):
                    rval = line.split()[-1][1:-1]
                    break
        finally:
            f.close()
    except:
        rval = '0'
    return rval

DESC_TITLE = 'SpikePlot : plotting package for spike sorting applications'
DESC_LONG = ''.join([DESC_TITLE, '\n\n', open('README', 'r').read()])

if __name__ == "__main__":
    setup(
        #main
        name='SpikePlot',
        version=find_version(),
        packages=['spikeplot'],
        install_requires=['scipy', 'matplotlib'],

        # metadata
        author='Philipp Meier',
        author_email='pmeier82@googlemail.com',
        maintainer='Philipp Meier',
        maintainer_email='pmeier82@googlemail.com',
        description=DESC_TITLE,
        long_description=DESC_LONG,
        license='MIT License',
        url='http://ni.tu-berlin.de',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Bio-Informatics'
        ])
