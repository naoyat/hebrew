#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew import *
from nose.tools import eq_, ok_, with_setup

def test_guess_word_form():
    eq_(UNKNOWN_FORM, guess_word_form(''))
    eq_(UNKNOWN_FORM, guess_word_form(' '))
    eq_(LATIN_FORM, guess_word_form('LoA'))
    eq_(LATIN_FORM, guess_word_form('Aa:NaH/:Nuw'))
    eq_(HEBREW_FORM, guess_word_form('הַשָּׁמַיִם'))

    eq_(UNKNOWN_FORM, guess_word_form(u''))
    eq_(UNKNOWN_FORM, guess_word_form(u' '))
    eq_(LATIN_FORM, guess_word_form(u'LoA'))
    eq_(LATIN_FORM, guess_word_form(u'Aa:NaH/:Nuw'))
    eq_(HEBREW_FORM, guess_word_form(u'הַשָּׁמַיִם'))
