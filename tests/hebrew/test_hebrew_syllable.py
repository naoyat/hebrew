#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.syllable import *
from hebrew.latin import cv_split, cv_unsplit
from nose.tools import eq_ #, ok_, with_setup

def test_divide_syllable():
    def T(word, expected_syllables):
        parts = cv_split(word, separate_yv=False)
        syllable_parts = divide_syllable(parts)
        syllables = map(cv_unsplit, syllable_parts)
        eq_(expected_syllables, ' - '.join(syllables))

    T('B+@A', 'B+@A')
    T('A@B', 'A@B')
    T('S@R@H', 'S@ - R@H')
    T('YiTS:H/@Q', 'YiTS: - H/@Q')
    T('D+@ViD', 'D+@ - ViD')
    T('UMoSHeH', 'U - Mo - SHeH')
    T('AaB:R@H@M', 'AaB: - R@ - H@M')
    T('Y:RuwSH@LaYiM', 'Y:Ruw - SH@ - La - YiM')
    T('Y:RiyH/ow', 'Y:Riy - H/ow')

    # p.25
    T('R:H/owB', 'R:H/owB')
    T('M:NaHeeL', 'M:Na - HeeL')
    T('T+:HiL+iyM', 'T+:Hi - L+iyM')
#    T('HaL:Luw', 'Ha - L:Luw')
    T('AaB:R@H@M', 'AaB: - R@ - H@M')
    T('MaH/:B+eReT', 'MaH/: - B+e - ReT')

    # p.26
    T('M:NowR@H', 'M:Now - R@H')
    T('Y:L@DiyM', 'Y:L@ - DiyM')
    T('MeLeK', 'Me - LeK')
    T('AaT+:', 'AaT+:')
    T('L@BaSH:T+:', 'L@ - BaSH:T+:')
    T('NeeP:TT:', 'NeeP:TT:')
    T('MiSS:K+eeN', 'MiSS: - K+eeN')
    T('MiD:B+@R', 'MiD: - B+@R')
    T('YiSH:M:Ruw', 'YiSH: - M:Ruw')
    T('NiSS:G+:Ruw', 'NiSS: - G+:Ruw')
    T('YiR:M:Y@Huw', 'YiR: - M:Y@ - Huw')
    # T('AeQ:SS:P+owR:TT', 'AeQ:SS: - P+owR:TT')
#    T('HaL:LuwY@H+', 'Ha - L:Luw - Y@H+')
    T('HiN:Nuw', 'Hi - N:Nuw')



