#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.latin import cv_split, cv_unsplit

MASC_SINGULAR = 0
FEM_SINGULAR = 1
MASC_PLURAL = 2
FEM_PLURAL = 3

def adj_form(masc_singular, i):
    if i == 0:
        return masc_singular

    parts = cv_split(masc_singular)
    print masc_singular, "->", parts

    if masc_singular[-2:] == 'eH':
        base = masc_singular[:-2]
    elif len(parts) == 2:
        base = masc_singular
    else:
        parts[0][1] = ':' # bad
        # parts[1][1] = ...
        base = cv_unsplit(parts)

    fem_singular = base + '@H' # bad
    if i == 1:
        return fem_singular

    if fem_singular[-2:] == '@H':
        base = fem_singular[:-2]
    elif fem_singular[-2:] == 'eT':
        base = fem_singular[:-2]
    elif fem_singular[-3:] == 'iyT':
        base = fem_singular[:-3] + 'iY+'
    else: # ??
        base = fem_singular[:-2]

    if i == 2:
        return base + 'iyM'
    else: # if i == 3:
        return base + 'owT'
