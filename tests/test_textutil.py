#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from textutil import *
from nose.tools import eq_, ok_, with_setup

def test_text_trans():
    sample = 'Abc, def, g. Hij, klmn!'
    eq_('ABC, DEF, G. HIJ, KLMN!', text_trans(lambda w:w.upper(), sample))
    eq_('abc, def, g. hij, klmn!', text_trans(lambda w:w.lower(), sample))
    eq_('***, ***, *. ***, ****!', text_trans(lambda w:re.sub(r'.', '*', w), sample))
    eq_('cbA, fed, g. jiH, nmlk!', text_trans(lambda w:w[::-1], sample))
    eq_('A-c, d-f, g-g. H-j, k-n!', text_trans(lambda w:w[0]+'-'+w[-1], sample))
    eq_('3, 3, 1. 3, 4!', text_trans(lambda w:str(len(w)), sample))

    sample = u'こんにちは, さようなら!'
    eq_(u'*****, *****!', text_trans(lambda w:re.sub(ur'.', '*', w), sample))
    eq_(u'はちにんこ, らなうよさ!', text_trans(lambda w:w[::-1], sample))
    eq_(u'こ…は, さ…ら!', text_trans(lambda w:w[0]+u'…'+w[-1], sample))
    eq_(u'5, 5!', text_trans(lambda w:str(len(w)), sample))
