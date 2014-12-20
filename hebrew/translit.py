#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import textutil

HEBREW_UC_TABLE = [
    # 0590
    None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None,
    # 05A0
    None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None,
    # 05B0
    ':', 'e:', 'a:', 'o:', 'i', 'ee', 'e', 'a',
    '@', 'o', 'o', 'u', '+', None, '-', None,
    # 05C0
    None, '<shin>', '<sin>', None, None, None, None, None,
    None, None, None, None, None, None, None, None,
    # 05D0
    'A', 'B', 'G', 'D', 'H', 'V', 'Z', 'H/',
    'TT', 'Y', 'K', 'K', 'L', 'M', 'M', 'N',
    # 05E0
    'N', 'SS', 'E', 'P', 'P', 'TS', 'TS', 'Q',
    'R', '$', 'T', None, None, None, None, None,
    # 05F0
    'VV', 'VY', 'YY', '\'', '\'\'', None, None, None,
    None, None, None, None, None, None, None, None,
]

HEBREW_POINT = {
    # SHEVA
    ':': u'\u05B0',
    # HATAF SEGOL
    'e:': u'\u05B1',
    # HATAF PATAH
    'a:': u'\u05B2',
    # HATAF QAMATS
    '@:': u'\u05B3', 'o:': u'\u05B3',
    # HIRIQ
    'i': u'\u05B4', 'iy': u'\u05B4\u05D9',
    # TSERE
    'ee': u'\u05B5', 'ey': u'\u05B5\u05D9',
    # SEGOL (3 triangle dots)
    'e': u'\u05B6',
    # PATAH
    'a': u'\u05B7',
    'ay': u'\u05B7\u05D9',
    'aay': u'\u05B7\u05D0\u05D9', # [ai]
    # QAMATS
    '@': u'\u05B8', # 'aa': u'\u05B8',
    '@y': u'\u05B8\u05D9',
    '@yv': u'\u05B8\u05D9\u05D5', # [av]
    # HOLAM HASER
    'o': u'\u05B9', # 'oa': u'\u05B9\u05D0',
    # HOLAM HASER for VAV
    'ow': u'\u05BA\u05D5',
    'oy': u'\u05BA\u05D5\u05D9',

    'uw': u'\u05D5\u05BC',
    'uy': u'\u05D5\u05BC\u05D9',
    # QUBUTS (three backslash dots)
    'u': u'\u05BB',
    # DAGESH or MAPIQ
    '+': u'\u05BC',
    # QAMATS QATAN
    #'o': u'\u05C7', ## not used

    '_': u'',
}

HEBREW_LETTER = {
    '-': u'\u05BE', # MAQAF

    'A': u'\u05D0', # ALEF
    'B': u'\u05D1', # BET
    'G': u'\u05D2', # GIMEL
    'D': u'\u05D3', # DALET
    'H': u'\u05D4', # HE
    'V': u'\u05D5', # VAV
    'Z': u'\u05D6', # ZAYIN
    'H/': u'\u05D7', # HET
    'TT': u'\u05D8', # TET
    'Y': u'\u05D9', # YOD
    'K': u'\u05DB', # KAF
    'L': u'\u05DC', # LAMED
    'M': u'\u05DE', # MEM
    'N': u'\u05E0', # NUN
    'SS': u'\u05E1', # SAMEKH
    'E': u'\u05E2', # AYIN
    'P': u'\u05E4', # PE
    'TS': u'\u05E6', # TSADI
    'Q': u'\u05E7', # QOF
    'R': u'\u05E8', # RESH
    'SH': u'\u05E9\u05C1', # SHIN + SHIN_DOT
    'S': u'\u05E9\u05C2', # SHIN + SIN_DOT
    'T': u'\u05EA', # TAV
}

HEBREW_LETTER_FINAL = {
    # KAF -> FINAL KAF
    u'\u05DB': u'\u05DA',
    # MEM -> FINAL MEM
    u'\u05DE': u'\u05DD',
    # NUN -> FINAL NUN
    u'\u05E0': u'\u05DF',
    # PE -> FINAL PE
    u'\u05E4': u'\u05E3',
    # TSADI -> FINAL TSADI
    u'\u05E6': u'\u05E5',
}


def parse_hebrew_word(word):
    chars = [ord(uc) for uc in word]
    parts = []
    # print word
    v = None
    c = None
    dotted = False
    for letter in word:
        uc = ord(letter)
        if uc < 0x0591 or uc > 0x05F4: continue
        if uc == 0x05F3:
            c += '\''
        elif uc == 0x05BC:
            dotted = True
            # c += '+'
        elif uc == 0x05C1:
            assert c == '$'
            c = 'SH'
        elif uc == 0x05C2:
            assert c == '$'
            c = 'S'
        elif 0x0590 <= uc < 0x05D0:
            # ofs = uc - 0x0590
            v = HEBREW_UC_TABLE[uc - 0x0590]
        elif 0x05D0 <= uc <= 0x05F4:
            if c:
                if dotted:
                    c += '+'
                dotted = False
                parts.append( (c, v) )
            c = HEBREW_UC_TABLE[uc - 0x0590]
            v = None
        else:
            pass
    if c:
        if dotted:
            c += '+'
        parts.append( (c, v) )
    # print parts

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
    lat = re.sub(r'H\+a$', 'AH+', lat)
    lat = re.sub(r'Ea$', 'AE', lat)
    lat = re.sub(r'H/a$', 'AH/', lat)

    if len(lat) > 0 and lat[-1] == '_':
        lat = lat[:-1]

    # print lat
    return lat


def trans_latin_to_hebrew(parts, with_vowel=False):
    buf = []
    l = len(parts)
    # print parts
    for i, (c, v) in enumerate(parts):
        if c[-1] == '+':
            c = c[:-1]
            dotted = True
        else:
            dotted = False
        if c[-1] == '\'':
            c = c[:-1]
            dashed = True
        else:
            dashed = False
        # print c, dotted, v
        hc = HEBREW_LETTER.get(c, u'?')
        if i == l-1:
            hc = HEBREW_LETTER_FINAL.get(hc, hc)
        buf.append(hc)
        if dotted:
            # print buf
            if len(buf) >= 1 and buf[-1][0] == u'\u05E9': # SHIN
                assert len(buf[-1]) == 2
                # print "insert before SHIN_DOT"
                shin_dot = buf[-1][1]
                buf[-1] = u'\u05E9'
                # insert before SHIN_DOT
                buf.append(HEBREW_POINT['+'])
                buf.append(shin_dot)
            else:
                buf.append(HEBREW_POINT['+'])
        if dashed:
            buf.append(u'\u05F3')

        if with_vowel and v:
            hv = HEBREW_POINT.get(v, u'?')
            buf.append(hv)
    # print ['%4x' % ord(uc) for uc in u''.join(buf)]
    return u''.join(buf)


def parse_latin_word(word, with_vowel=False, debug=False):
    parts = []
    # furtive patah
    word = word.replace('AH+', 'H+a').replace('AE', 'Ea').replace('AH/', 'H/a')

    word = word.replace('-', '-_')

    word = word.replace('iy', 'iY_')
    word = word.replace('uy', 'uwY_')
    word = word.replace('oy', 'owY_')
    # word = word.replace('ow', 'oV_')
    # word = word.replace('oa', 'oA_')
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
            parts.append( (c[:-1], None) )
            c = '-'
            v = None
        i += mo.end()

        mo = re.match('([^-A-Z+/]|_)+', word[i:])
        if mo:
            v = mo.group(0)
            i += mo.end()
        else:
            v = None
        parts.append( (c,v) )

    if debug:
        print parts

    hs = trans_latin_to_hebrew(parts, with_vowel=with_vowel)
    return hs


def parse_latin_text(latin_text, with_vowel=False, debug=False):
    return textutil.text_trans(lambda word: parse_latin_word(word, with_vowel=with_vowel, debug=debug), latin_text)


def parse_hebrew_text(hebrew_text, vowel=False):
    return textutil.text_trans(parse_hebrew_word, hebrew_text)
