#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

def cv_split(word, separate_yv=True):
    parts = []
    # furtive patah
    word = word.replace('AH+', 'H+a').replace('AE', 'Ea').replace('AH/', 'H/a')

    word = word.replace('-', '-_')

    word = word.replace('U', 'V+_') # 語頭のみ

    if separate_yv:
        word = word.replace('iy', 'iY_')
        word = word.replace('uy', 'uwY_')
        word = word.replace('oy', 'owY_')
        # word = word.replace('ow', 'oV_')
        word = word.replace('uw', '_V+_')
        word = word.replace('aay', 'aA_Y_')
        word = word.replace('ay', 'aY_')
        word = word.replace('@yv', '@Y_V_')
        word = word.replace('@y', '@Y_')

    # print word
    i = 0
    while True:
        mo = re.match('[-A-Z+/\']+', word[i:])
        if not mo: break
        c = mo.group(0)
        if len(c) >= 2 and c[-1] == '-':
            parts.append( [c[:-1], None] )
            c = '-'
            v = None
        i += mo.end()

        mo = re.match('([^-A-Z+/]|_)+', word[i:])
        if mo:
            v = mo.group(0)
            i += mo.end()
        else:
            v = None

        if v == '_': v = None
        parts.append( [c, v] )

    return parts


def cv_unsplit(parts):
    if all([v is None for c,v in parts]):
        lat = ''.join([c + '_' for c,v in parts])
    else:
        lat = ''.join([c + (v or '_') for c,v in parts])

    # long vowels with Y/V/A
    lat = lat.replace('iY_', 'iy')
    lat = lat.replace('oV_', 'ow')
    # lat = lat.replace('oA_', 'oa')
    lat = lat.replace('_V+_', 'uw')
    lat = lat.replace('aY_', 'ay')
    lat = lat.replace('aA_Y_', 'aay')
    lat = lat.replace('@Y_V_', '@yv')
    lat = lat.replace('@Y_', '@y')
    lat = lat.replace('eeY_', 'ey')
    lat = lat.replace('owY_', 'oy')
    lat = lat.replace('uwY_', 'uy')
    # furtive patah
    if len(lat) > 2:
        lat = re.sub(r'Ea$', 'AE', lat)
        if len(lat) > 3:
            lat = re.sub(r'H\+a$', 'AH+', lat)
            lat = re.sub(r'H/a$', 'AH/', lat)

    lat = re.sub(r'K:$', 'K', lat)
    lat = re.sub(r'^V\+_', 'U', lat)

    if len(lat) > 0 and lat[-1] == '_':
        lat = lat[:-1]

    return lat
