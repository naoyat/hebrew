#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.translit import *
from nose.tools import eq_, ok_, with_setup
import random
import copy

#def _wrap(s):
#   # RLM + s + LRM
#   return u'\u200F%s\u200E' % s

TEST_DATA_PATH = 'tests/data/translit_testdata.txt'

test_data_table = []

def setup():
    global test_data_table
    with open(TEST_DATA_PATH, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '': continue
            if line[0] == '#': continue ##
            lat, _heb = line.split('\t')
            heb = _heb.decode('utf-8')
            test_data_table.append( (lat, heb) )

def teardown():
    pass


def _individual_test(fn_to_test, testcases):
    for before, after in testcases:
        eq_(after, fn_to_test(before))

def _random_concat_test(fn_to_test, testcases, delim=u''):
    random.shuffle(testcases)
    before_text = delim.join([before for before, _ in testcases])
    after_text = delim.join([after for _, after in testcases])
    eq_(after_text, fn_to_test(before_text))


def test_unligature():
    testcases = [
        (unichr(0xFB1D + offset), lig) for offset, lig in enumerate(HEBREW_UNLIGATURE_TABLE)
    ]
    _individual_test(unligature, testcases)
    _random_concat_test(unligature, testcases)


def test_ligature():
    testcases = copy.copy(HEBREW_LIGATURE_TABLE)
    _individual_test(ligature, testcases)
    _random_concat_test(ligature, testcases)


def test_parse_hebrew_word():
    for expected_lat, heb in test_data_table:
        if re.search('[ ,.]', expected_lat): continue
        result = parse_hebrew_word(heb)
        if result[-1] == '_': result = result[:-1]
        eq_(expected_lat, result)


#def test_latin_parts_to_hebrew():
#    TO BE IMPLEMENTED
#    pass


def test_parse_latin_word():
    for lat, expected_heb in test_data_table:
        if re.search('[ ,.]', lat): continue
        result = parse_latin_word(lat, with_vowel=True)
        eq_(expected_heb, result)


@with_setup(setup, teardown)
def test_parse_hebrew_text():
    def _wrapper(hebrew):
        result = parse_hebrew_text(hebrew)
        if result[-1] == '_': result = result[:-1]
        # print u"result: u'%s'" % result,
        # print u"\texpected: u'%s'" % expected_latin
        return result

    testcases = [(heb, lat) for lat, heb in test_data_table]

    _individual_test(_wrapper, testcases)
    _random_concat_test(_wrapper, testcases, u' ')


@with_setup(setup, teardown)
def test_parse_latin_text():
    def _wrapper(latin):
        result = parse_latin_text(latin, with_vowel=True)
        # print u"result: u'%s'" % result,
        # print u"\texpected: u'%s'" % expected_hebrew
        return result

    testcases = copy.copy(test_data_table)

    _individual_test(_wrapper, testcases)
    _random_concat_test(_wrapper, testcases, u' ')


def test_bereshit():
	latin_text = 'B+:ReeA_SHiyT, B+@R@A Ae:LoHiyM, AeeT HaSH+@MaYiM, V:AeeT H@A@ReTS.'
	hebrew_text = u'בְּרֵאשִׁית, בָּרָא אֱלֹהִים, אֵת הַשָּׁמַיִם, וְאֵת הָאָרֶץ.'

	eq_(hebrew_text, parse_latin_text(latin_text, True))
	eq_(latin_text, parse_hebrew_text(hebrew_text))


