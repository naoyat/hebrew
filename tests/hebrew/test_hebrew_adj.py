#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.adj import *
from nose.tools import eq_, ok_, with_setup
from tests import weak_eq_

def test_adj_form():
    def T(masc_sg, fem_sg, masc_pl, fem_pl):
        weak_eq_(fem_sg, adj_form(masc_sg, FEM_SINGULAR))
        weak_eq_(masc_pl, adj_form(masc_sg, MASC_PLURAL))
        weak_eq_(fem_pl, adj_form(masc_sg, FEM_PLURAL))

    # 良い
    T('TowB', 'TowB@H', 'TowBiyM', 'TowBowT')
    # 大きい
    T('G+@DowL', 'G+:DowL@H', 'G+:DowLiyM', 'G+:DowLowT')
    # 小さい
    T('Q@TT@N', 'Q:TTaN+@H', 'Q:TTaN+iyM', 'Q:TTaN+owT')
    # 新しい
    T('H/@D@SH', 'H/a:D@SH@H', 'H/a:D@SHiyM', 'H/a:D@SHowT')
    # 美しい
    T('Y@PeH', 'Y@P@H', 'Y@PiyM', 'Y@PowT')
