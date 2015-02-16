#!/usr/bin/python
# -*- coding: utf-8 -*-
# from hebrew import guess_word_form, LATIN_FORM
from hebrew.latin import cv_split, cv_unsplit

DEBUG = False

def plural_form(lat_sg):
    # assert isinstance(lat_sg, unicode)
    # assert guess_word_form(lat_sg) == LATIN_FORM

    parts = cv_split(lat_sg)

    if DEBUG:
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

    if DEBUG:
        print base

    if is_female_form:
        # return base_form + u'owT'
        base[-1][1] = 'o'
        base += [['V', None], ['T', None]]
    else:
        # return base_form + u'iyM'
        base[-1][1] = 'i'
        base += [['Y', None], ['M', None]]

    if DEBUG:
        print base

    dest_lat = cv_unsplit(base)
    if DEBUG:
        print dest_lat

    return dest_lat


def affix_ha_article(lat_without_ha):
    # assert guess_word_form(lat_without_ha) == LATIN_FORM

    # 固有名詞なら ha- をつけずに返す処理をしたい

    parts = [['H', 'a']] + cv_split(lat_without_ha)
    if parts[1][0][-1] != '+':
        parts[1][0] += '+'

    lat_with_ha = cv_unsplit(parts)
    if DEBUG:
        print lat_with_ha

    return lat_with_ha


def unfix_ha_article(lat_with_ha):
    # assert guess_word_form(lat_with_ha) == LATIN_FORM

    # 固有名詞なら ha- をつけずに返す処理をしたい
    parts = cv_split(lat_with_ha)
    if parts[0] != ['H', 'a']:
        return False, lat_with_ha

    parts = parts[1:]

    if parts[0][0][-1] == '+':
        parts[0][0] = parts[0][0][:-1] # そうでない場合もある
        # ここ、辞書を見るなりしてチェックしないと駄目だ
        # T+aL:MiyDiyM
        # T+MuwNowT

    lat_without_ha = cv_unsplit(parts)
    if DEBUG:
        print lat_without_ha

    return True, lat_without_ha


def affix_ve(lat_without_ve):
    # assert guess_word_form(lat_without_ve) == LATIN_FORM

    parts = cv_split(lat_without_ve)
    if parts[0][0] in ('B+', 'K+', 'P+'):
        parts[0][0] = parts[0][0].replace('+', '')

    if parts[0][0] in ('B', 'V', 'M', 'P') or parts[0][1] == ':':
        parts = [['V+', None]] + parts
    else:
        parts = [['V', ':']] + parts

    lat_with_ve = cv_unsplit(parts)

    if DEBUG:
        print lat_with_ve

    return lat_with_ve


def unfix_ve(lat_with_ve):
    parts = cv_split(lat_with_ve)
    assert len(parts) >= 2

    if parts[0] not in (['V+', None], ['V', ':']):
        # raise "you don't have to do this"
        # return lat_with_ve
        return False, lat_with_ve

    if parts[1][0] in ('B', 'V', 'M', 'P') or parts[1][1] == ':':
        u_start = True
    else:
        u_start = False

    if parts[0] == ['V+', None]: # u-
        assert u_start
    else: # ve-
        assert not u_start

    if parts[1][0] in ('B', 'K', 'P'):
        parts[1][0] += '+'

    parts = parts[1:]
    lat_without_ve = cv_unsplit(parts)

    if DEBUG:
        print lat_without_ve

    return True, lat_without_ve
