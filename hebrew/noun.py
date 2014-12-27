#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew import guess_word_form, LATIN_FORM
from hebrew.latin import cv_split, cv_unsplit


def plural_form(lat_sg, debug=False):
#    assert isinstance(lat_sg, unicode)
    assert guess_word_form(lat_sg) == LATIN_FORM

    parts = cv_split(lat_sg)

    if debug:
        print ">", lat_sg

    is_female_form = False
    if lat_sg[-2:] == '@H':
        # -@H -> 0
        base_form = lat_sg[:-2]
        base = parts[:-1]
        base[-1][1] = None
        is_female_form = True
    elif lat_sg[-2:] == 'eH':
        # -eH -> -0
        base_form = lat_sg[:-2]
        base = parts[:-1]
        base[-1][1] = None
#        is_female_form = True
    elif lat_sg[-2:] in ('aT', 'eT'):
        #  -aT/eT -> -@
        base_form = lat_sg[:-2]
        base = parts[:-1]
        base[-1][1] = None
        base[-2][1] = '@'
        is_female_form = True
    elif lat_sg[-3:] == 'iyT':
        # -iyT (?i.Y.T) -> (?i.YY)
        base_form = lat_sg[:-3]
        base = parts[:-1]
        base[-1] = ['Y+', None]
        is_female_form = True
    elif lat_sg[-3:] == 'uwT':
        # -uwT (?.VV.T) -> (?u.YY)
        base_form = lat_sg[:-3]
        base = parts[:-1]
        base[-2][1] = 'u'
        base[-1] = ['Y+', None]
        is_female_form = True
    else:
        base_form = lat_sg
        base = parts

    if len(base) >= 3:
        if base[0][1] == '@':
            base[0][1] = 'a'
        elif base[0][1] in ('e', 'ee') and base[1][1] in ('e', 'ee'):
            # 最後の２つが -e-e-
            base[0][1] = ':'
            base[1][1] = '@'
        elif base[-1][1] is None and base[-2][1] == ':':
            # 最後の母音が ':''
            base[0][1] = ':'
            base[1][1] = '@'
            if base[-1][0][-1] == '+':
                base[-1][0] = base[-1][0][:-1]

    if debug:
        print base

    if is_female_form:
        # return base_form + u'owT'
        base[-1][1] = 'o'
        base += [['V', None], ['T', None]]
    else:
        # return base_form + u'iyM'
        base[-1][1] = 'i'
        base += [['Y', None], ['M', None]]

    if debug:
        print base

    dest_lat = cv_unsplit(base)
    if debug:
        print dest_lat

    return dest_lat


def ha_article(lat_without_ha, debug=False):
    assert guess_word_form(lat_without_ha) == LATIN_FORM

    # 固有名詞なら ha- をつけずに返す処理をしたい

    parts = [['H', 'a']] + cv_split(lat_without_ha)
    if parts[1][0][-1] != '+':
        parts[1][0] += '+'

    lat_with_ha = cv_unsplit(parts)
    if debug:
        print lat_with_ha

    return lat_with_ha


def with_ve(lat_without_ve, debug=False):
    assert guess_word_form(lat_without_ve) == LATIN_FORM

    parts = cv_split(lat_without_ve)
    if parts[0][0] in ('B+', 'K+', 'P+'):
        parts[0][0] = parts[0][0].replace('+', '')

    if parts[0][0] in ('B', 'V', 'M', 'P') or parts[0][1] == ':':
        parts = [['V+', None]] + parts
    else:
        parts = [['V', ':']] + parts

    lat_with_ve = cv_unsplit(parts)

    if debug:
        print lat_with_ve

    return lat_with_ve


