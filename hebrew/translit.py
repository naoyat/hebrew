#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import textutil
from latin import cv_split, cv_unsplit

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

HEBREW_UNLIGATURE_TABLE = [
    # \uFB1D 〜 \uFB4F
    u'\u05D9\u05B4', # FB1D יִ HEBREW LETTER YOD WITH HIRIQ
    u'\u05BF',       # FB1E $ﬞ HEBREW POINT JUDEO-SPANISH VARIKA
                     # a glyph variant of 05BF 
    u'\u05F2\u05B7', # FB1F ײַ HEBREW LIGATURE YIDDISH YOD YOD PATAH
    u'\u05E2',       # FB20 ע HEBREW LETTER ALTERNATIVE AYIN
                     # this form of AYIN has no descender,
                     # for use with marks placed below the letter
    u'\u05D0',       # FB21 א HEBREW LETTER WIDE ALEF
    u'\u05D3',       # FB22 ד HEBREW LETTER WIDE DALET
    u'\u05D4',       # FB23 ה HEBREW LETTER WIDE HE
    u'\u05DB',       # FB24 כ HEBREW LETTER WIDE KAF
    u'\u05DC',       # FB25 ל HEBREW LETTER WIDE LAMED
    u'\u05DD',       # FB26 ם HEBREW LETTER WIDE FINAL MEM
    u'\u05E8',       # FB27 ר HEBREW LETTER WIDE RESH
    u'\u05EA',       # FB28 ת HEBREW LETTER WIDE TAV
    u'+',            # FB29 ﬩ HEBREW LETTER ALTERNATIVE PLUS SIGN
    u'\u05E9\u05C1', # FB2A שׁ HEBREW LETTER SHIN WITH SHIN DOT
    u'\u05E9\u05C2', # FB2B שׂ HEBREW LETTER SHIN WITH SIN DOT
    #u'\uFB49\u05C1', # FB2C שּׁ HEBREW LETTER SHIN WITH DAGESH AND SHIN DOT
    u'\u05E9\u05BC\u05C1', # FB2C שּׁ HEBREW LETTER SHIN WITH DAGESH AND SHIN DOT
    #u'\uFB49\u05C2', # FB2D שּׂ HEBREW LETTER SHIN WITH DAGESH AND SIN DOT
    u'\u05E9\u05BC\u05C2', # FB2D שּׂ HEBREW LETTER SHIN WITH DAGESH AND SIN DOT
    u'\u05D0\u05B7', # FB2E אַ HEBREW LETTER ALEF WITH PATAH
    u'\u05D0\u05B8', # FB2F אָ HEBREW LETTER ALEF WITH QAMATS
    u'\u05D0\u05BC', # FB30 אּ HEBREW LETTER ALEF WITH MAPIQ
    u'\u05D1\u05BC', # FB31 בּ HEBREW LETTER BET WITH DAGESH
    u'\u05D2\u05BC', # FB32 גּ HEBREW LETTER GIMEL WITH DAGESH
    u'\u05D3\u05BC', # FB33 דּ HEBREW LETTER DALET WITH DAGESH
    u'\u05D4\u05BC', # FB34 הּ HEBREW LETTER HE WITH MAPIQ
    u'\u05D5\u05BC', # FB35 וּ HEBREW LETTER VAV WITH DAGESH
    u'\u05D6\u05BC', # FB36 זּ HEBREW LETTER ZAYIN WITH DAGESH
    u'\uFB37',       # FB37 " <reserved>
    u'\u05D8\u05BC', # FB38 טּ HEBREW LETTER TET WITH DAGESH
    u'\u05D9\u05BC', # FB39 יּ HEBREW LETTER YOD WITH DAGESH
    u'\u05DA\u05BC', # FB3A ךּ HEBREW LETTER FINAL KAF WITH DAGESH
    u'\u05DB\u05BC', # FB3B כּ HEBREW LETTER KAF WITH DAGESH
    u'\u05DC\u05BC', # FB3C לּ HEBREW LETTER LAMED WITH DAGESH
    u'\uFB3D',       # FB3D " <reserved>
    u'\u05DE\u05BC', # FB3E מּ HEBREW LETTER MEM WITH DAGESH
    u'\uFB3F',       # FB3F " <reserved>
    u'\u05E0\u05BC', # FB40 נּ HEBREW LETTER NUN WITH DAGESH
    u'\u05E1\u05BC', # FB41 סּ HEBREW LETTER SAMEKH WITH DAGESH
    u'\uFB42',       # FB42 " <reserved>
    u'\u05E3\u05BC', # FB43 ףּ HEBREW LETTER FINAL PE WITH DAGESH
    u'\u05E4\u05BC', # FB44 פּ HEBREW LETTER PE WITH DAGESH
    u'\uFB45',       # FB45 " <reserved>
    u'\u05E6\u05BC', # FB46 צּ HEBREW LETTER TSADI WITH DAGESH
    u'\u05E7\u05BC', # FB47 קּ HEBREW LETTER QOF WITH DAGESH
    u'\u05E8\u05BC', # FB48 רּ HEBREW LETTER RESH WITH DAGESH
    u'\u05E9\u05BC', # FB49 שּ HEBREW LETTER SHIN WITH DAGESH
    u'\u05D5\u05B9', # FB4B וֹ HEBREW LETTER VAV WITH HOLAM
    u'\u05D1\u05BF', # FB4C בֿ HEBREW LETTER BET WITH RAFE
    u'\u05DB\u05BF', # FB4D כֿ HEBREW LETTER KAF WITH RAFE
    u'\u05E4\u05BF', # FB4E פֿ HEBREW LETTER PE WITH RAFE
    u'\u05D0\u05DC', # FB4F אל HEBREW LIGATURE ALEF LAMED
]

HEBREW_LIGATURE_TABLE = [
    (u'\u05D9\u05B4', u'\uFB1D'), # יִ HEBREW LETTER YOD WITH HIRIQ
    #(u'\u05BF', u'\uFB1E') # $ﬞ HEBREW POINT JUDEO-SPANISH VARIKA
                     # a glyph variant of 05BF 
    (u'\u05F2\u05B7', u'\uFB1F'), # ײַ HEBREW LIGATURE YIDDISH YOD YOD PATAH
    #(u'\u05E2', u'\uFB20') # ע HEBREW LETTER ALTERNATIVE AYIN
                     # this form of AYIN has no descender,
                     # for use with marks placed below the letter
    (u'\u05E9\u05C1', u'\uFB2A'), # שׁ HEBREW LETTER SHIN WITH SHIN DOT
    (u'\u05E9\u05C2', u'\uFB2B'), # שׂ HEBREW LETTER SHIN WITH SIN DOT
    # (u'\uFB49\u05C1', u'\uFB2C'), # שּׁ HEBREW LETTER SHIN WITH DAGESH AND SHIN DOT
    (u'\u05E9\u05BC\u05C1', u'\uFB2C'), # שּׁ HEBREW LETTER SHIN WITH DAGESH AND SHIN DOT
    # (u'\uFB49\u05C2', u'\uFB2D'), # שּׂ HEBREW LETTER SHIN WITH DAGESH AND SIN DOT
    (u'\u05E9\u05BC\u05C2', u'\uFB2D'), # שּׂ HEBREW LETTER SHIN WITH DAGESH AND SIN DOT
    (u'\u05D0\u05B7', u'\uFB2E'), # אַ HEBREW LETTER ALEF WITH PATAH
    (u'\u05D0\u05B8', u'\uFB2F'), # אָ HEBREW LETTER ALEF WITH QAMATS
    (u'\u05D0\u05BC', u'\uFB30'), # אּ HEBREW LETTER ALEF WITH MAPIQ
    (u'\u05D1\u05BC', u'\uFB31'), # בּ HEBREW LETTER BET WITH DAGESH
    (u'\u05D2\u05BC', u'\uFB32'), # גּ HEBREW LETTER GIMEL WITH DAGESH
    (u'\u05D3\u05BC', u'\uFB33'), # דּ HEBREW LETTER DALET WITH DAGESH
    (u'\u05D4\u05BC', u'\uFB34'), # הּ HEBREW LETTER HE WITH MAPIQ
    (u'\u05D5\u05BC', u'\uFB35'), # וּ HEBREW LETTER VAV WITH DAGESH
    (u'\u05D6\u05BC', u'\uFB36'), # זּ HEBREW LETTER ZAYIN WITH DAGESH
    (u'\uFB37',       u'\uFB37'), # " <reserved>
    (u'\u05D8\u05BC', u'\uFB38'), # טּ HEBREW LETTER TET WITH DAGESH
    (u'\u05D9\u05BC', u'\uFB39'), # יּ HEBREW LETTER YOD WITH DAGESH
    (u'\u05DA\u05BC', u'\uFB3A'), # ךּ HEBREW LETTER FINAL KAF WITH DAGESH
    (u'\u05DB\u05BC', u'\uFB3B'), # כּ HEBREW LETTER KAF WITH DAGESH
    (u'\u05DC\u05BC', u'\uFB3C'), # לּ HEBREW LETTER LAMED WITH DAGESH
    (u'\uFB3D',       u'\uFB3D'), # " <reserved>
    (u'\u05DE\u05BC', u'\uFB3E'), # מּ HEBREW LETTER MEM WITH DAGESH
    (u'\uFB3F',       u'\uFB3F'), # " <reserved>
    (u'\u05E0\u05BC', u'\uFB40'), # נּ HEBREW LETTER NUN WITH DAGESH
    (u'\u05E1\u05BC', u'\uFB41'), # סּ HEBREW LETTER SAMEKH WITH DAGESH
    (u'\uFB42',       u'\uFB42'), # " <reserved>
    (u'\u05E3\u05BC', u'\uFB43'), # ףּ HEBREW LETTER FINAL PE WITH DAGESH
    (u'\u05E4\u05BC', u'\uFB44'), # פּ HEBREW LETTER PE WITH DAGESH
    (u'\uFB45',       u'\uFB45'), # " <reserved>
    (u'\u05E6\u05BC', u'\uFB46'), # צּ HEBREW LETTER TSADI WITH DAGESH
    (u'\u05E7\u05BC', u'\uFB47'), # קּ HEBREW LETTER QOF WITH DAGESH
    (u'\u05E8\u05BC', u'\uFB48'), # רּ HEBREW LETTER RESH WITH DAGESH
    (u'\u05E9\u05BC', u'\uFB49'), # שּ HEBREW LETTER SHIN WITH DAGESH
    (u'\u05D5\u05B9', u'\uFB4B'), # וֹ HEBREW LETTER VAV WITH HOLAM
    (u'\u05D1\u05BF', u'\uFB4C'), # בֿ HEBREW LETTER BET WITH RAFE
    (u'\u05DB\u05BF', u'\uFB4D'), # כֿ HEBREW LETTER KAF WITH RAFE
    (u'\u05E4\u05BF', u'\uFB4E'), # פֿ HEBREW LETTER PE WITH RAFE
    (u'\u05D0\u05DC', u'\uFB4F'), # אל HEBREW LIGATURE ALEF LAMED
]


def unligature(text):
    return u''.join([
        HEBREW_UNLIGATURE_TABLE[ord(ch)-0xFB1D] if 0xFB1D <= ord(ch) <= 0xFB4F else ch
        for ch in text
        ])


def ligature(text):
    # naive impl.
    for before, after in HEBREW_LIGATURE_TABLE:
        text = text.replace(before, after)
    return text


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

    return cv_unsplit(parts)


def latin_parts_to_hebrew(parts, with_vowel=True):
    buf = []
    last = len(parts) - 1
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
        if i == last:
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

        if with_vowel:
            if v:
                hv = HEBREW_POINT.get(v, u'?')
                buf.append(hv)
            elif i == last and c == 'K':
                hv = HEBREW_POINT[':']
                buf.append(hv)

    # print ['%4x' % ord(uc) for uc in u''.join(buf)]
    return u''.join(buf)


def parse_latin_word(word, with_vowel=True, debug=False):
    parts = cv_split(word)
    if debug:
        print parts

    hs = latin_parts_to_hebrew(parts, with_vowel=with_vowel)
    return hs


def parse_hebrew_text(hebrew_text, with_vowel=True):
    return textutil.text_trans(parse_hebrew_word, hebrew_text)


def parse_latin_text(latin_text, with_vowel=True, debug=False):
    return textutil.text_trans(lambda word: parse_latin_word(word, with_vowel=with_vowel, debug=debug), latin_text)
