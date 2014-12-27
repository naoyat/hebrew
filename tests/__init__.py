from nose.tools import eq_

def weak_eq_(expected, actual):
    # ignoring dagesh
    eq_(expected.replace('+', ''), actual.replace('+', ''))

