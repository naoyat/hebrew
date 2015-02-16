#!/usr/bin/python
# -*- coding: utf-8 -*-
#from hebrew.noun import unfix_ha_article
from hebrew.latin import cv_split, cv_unsplit

def affix_preposition(prep, word):
#    is_ha_affixed, word_without_ha = unfix_ha(word)
    parts = cv_split(word)
    if parts[0][0] == 'H': #, 'a']:
        is_ha_affixed = True
        ha_vowel = parts[0][1]
        base_parts = parts[1:]
    else:
        is_ha_affixed = False
        base_parts = parts

    if prep == 'B+:-':  # 〜の中で
        if is_ha_affixed:
            prep_parts = [['B+', ha_vowel]]
        else:
            prep_parts = [['B+', ':']]
    elif prep == 'K+:-':  # 〜の如く
        if is_ha_affixed:
            prep_parts = [['K+', ha_vowel]]
        else:
            prep_parts = [['K+', ':']]
    elif prep == 'L:-':  # 〜へ
        if is_ha_affixed:
            prep_parts = [['L', ha_vowel]]
        else:
            prep_parts = [['L', ':']]
    elif prep in ('MiN', 'Mi-'):  # 〜から
        if is_ha_affixed:
            prep_parts = [['M', 'ee'], parts[0]]
        else:
            if base_parts[0][0] in ('A', 'H', 'H/', 'E', 'R'):
                prep_parts = [['M', 'ee']]
            else:
                prep_parts = [['M', 'i']]
    else:
        pass

    parts = prep_parts + base_parts
    return cv_unsplit(parts)
