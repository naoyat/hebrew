#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.prep import *
from nose.tools import eq_, ok_, with_setup
from tests import weak_eq_

def test_affix_preposition():
    #prep, word):
    def T(word, prep, expected):
        weak_eq_(expected, affix_preposition(prep, word))

    # b/k/l + (word)
    T('K+iT+@H', 'B+:-', 'B+:KiT+@H')
    T('YaP+@N', 'L:-', 'L:YaP+@N')
    T('MoSHeH', 'K+:-', 'K+:MoSHeH')

    # b/k/l + (ha-word)
    T('HaK+iT+@H', 'B+:-', 'B+aK+iT+@H')
    T('H@A@ReTS', 'B+:-', 'B+@A@ReTS')
    T('H@EiyR', 'L:-', 'L@EiyR')
    T('HaM+owReH', 'K+:-', 'K+aM+owReH')

    # min + (word)
    T('K+iT+@H', 'MiN', 'MiK+iT+@H')
    T('MiTT+@H', 'MiN', 'MiM+iTT+@H')

    T('Aa:MeRiyQ@H', 'Mi-', 'MeeAa:MeRiyQ@H')
    T('EiyR', 'Mi-', 'MeeEiyR')
    T('RaK+eBeT', 'Mi-', 'MeeRaK+eBeT')

    T('HaB+aYiT', 'Mi-', 'MeeHaB+aYiT')
    T('HaH/a:BeeR@H', 'Mi-', 'MeeHaH/a:BeeR@H')
    T('H@AuL:P+@N', 'Mi-', 'MeeH@AuL:P+@N')