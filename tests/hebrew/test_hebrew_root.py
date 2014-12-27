#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.root import *
from nose.tools import eq_, ok_, with_setup


def test_pel():
    r = Root('PEL')
    eq_('P', r.p)
    eq_('E', r.e)
    eq_('L', r.l)

    r = Root('LMD')
    eq_('L', r.p)
    eq_('M', r.e)
    eq_('D', r.l)

    r = Root('SH M R')
    eq_('SH', r.p)
    eq_('M', r.e)
    eq_('R', r.l)


def test_getitem():
    r = Root('LMD')
    eq_('L', r[0])
    eq_('M', r[1])
    eq_('D', r[2])

    r = Root('SH M R')
    eq_('SH', r[0])
    eq_('M', r[1])
    eq_('R', r[2])


def test_repr():
    r = Root('LMD')
    eq_('L M D', repr(r))

    r = Root('SH M R')
    eq_('SH M R', repr(r))


def test_inject():
    r = Root('LMD')
    eq_('LowMeeD', r.inject('_ow_ee_'))
    eq_('LowMeeD', r.inject('_ow_ee_'.split('_')))
    eq_('LMD', r.inject('___'))
    eq_('MiT:L+aM+:DiyM', r.inject('MiT:_+a_+:_iyM'))
