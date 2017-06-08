# -*- coding: utf-8 -*-
#
# xml2dict/__init__.py
#
"""
XML to Dict Parser package
"""
__docformat__ = "restructuredtext en"

__all__ = ('__version__', '__author__', '__email__', '__license__',
           '__credits__', 'XML2Dict',)

from .xml2dict import *


__version_info__ = {
    'major': 1,
    'minor': 0,
    'patch': 0,
    'releaselevel': 'final',
    'serial': 1
    }


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = []
    vers.append("{major:d}".format(**__version_info__))
    vers.append("{minor:d}".format(**__version_info__))

    if __version_info__.get('patch', 0):
        vers.append("{patch:d}".format(**__version_info__))

    result = '.'.join(vers)

    if __version_info__.get('releaselevel') != 'final' and not short:
        result += "{}{:d}".format(
            __version_info__.get('releaselevel', 'a')[0],
            __version_info__.get('serial'))

    return result

__version__ = get_version()
