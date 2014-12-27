#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import textutil
import hebrew.translit

hebdic = {}
latdic = {}

UNKNOWN_FORM = 0
HEBREW_FORM  = 1
LATIN_FORM   = 2

def guess_word_form(word):
    if isinstance(word, str):
        word = word.decode('utf-8')
    if len(word) == 0: return UNKNOWN_FORM

    last_char_code = [ord(ch) for ch in word][-1]
    if last_char_code <= 0x20:
        return UNKNOWN_FORM
    elif last_char_code <= 0x7f:
       return LATIN_FORM
    elif 0x0590 <= last_char_code <= 0x05FF:
       return HEBREW_FORM
    else:
       return UNKNOWN_FORM


def dict_stream(path=None):
    if not path: path = 'dict.tsv'

    with open(path, 'r') as f:
        for line in f:
            line = line.rstrip()
            if len(line) == 0 or line[0] == '#': continue
            lat_utf8, pos, trans_utf8 = line.split('\t')
            lat = lat_utf8.decode('utf-8')
            trans = trans_utf8.decode('utf-8')
            heb = translit.parse_latin_text(lat, with_vowel=True)
            yield heb, lat, pos, trans

def load_dict(path=None):
    global hebdic, latdic
    for heb, lat, pos, trans in dict_stream(path):
        # print ('(%s) (%s) %s. %s' % (lat, heb, pos, trans)).encode('utf-8')
        # print '%s,%s' % (lat, heb)
        entry = (heb, lat, pos, None, trans)
        hebdic[heb] = entry
        latdic[lat] = entry

def lookup_word_heb(word_heb):
    if isinstance(word_heb, str):
        word_heb = word_heb.decode('utf-8')
#    print word_heb
    if hebdic.has_key(word_heb):
        return hebdic[word_heb]
    else:
        lat = translit.parse_hebrew_text(heb)
        return (word_heb, lat, '*', None, '*')

def lookup_word_lat(word_lat):
    if isinstance(word_lat, str):
        word_lat = word_lat.decode('utf-8')

    ans = ['#MULTI#']

    ve = False
    if word_lat[:2] == u'V:':
        ve = True
        word_lat = word_lat[2:]
    elif word_lat[0] == u'U':
        ve = True
        word_lat = word_lat[1:]
        if re.match(r'[BKP]', word_lat):
            word_lat = word_lat[0] + '+' + word_lat[1:]

    if ve:
        ans.append( (u'V:', 'V:', 'conj', None, u'and') )

    if latdic.has_key(word_lat):
        ans.append( latdic[word_lat] )
    else:
        heb = translit.parse_latin_text(word_lat, with_vowel=True)
        ans.append( (heb, word_lat, '*', None, '*') )

    if len(ans) > 2:
        return ans
    else:
        return ans[1]

def lookup_text_heb(text_heb):
    return textutil.text_trans(lookup_word_heb, text_heb, do_join=False)

def lookup_text_lat(text_lat):
    return textutil.text_trans(lookup_word_lat, text_lat, do_join=False)


if __name__ == '__main__':
    load_dict()

