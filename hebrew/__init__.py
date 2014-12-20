#!/usr/bin/python
# -*- coding: utf-8 -*-
import textutil
import hebrew.translit

hebdic = {}
latdic = {}


def dict_stream(path='dict.tsv'):
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
        print ('(%s) (%s) %s. %s' % (lat, heb, pos, trans)).encode('utf-8')
        # print '%s,%s' % (lat, heb)
        hebdic[heb] = (pos, None, trans)
        latdic[lat] = (pos, None, trans)

def lookup_word_heb(word_heb):
    return hebdic.get(word_heb, None)

def lookup_word_lat(word_lat):
    return latdic.get(word_lat, None)

def lookup_text_heb(text_heb):
    pass

if __name__ == '__main__':
    load_dict()

