#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.root import Root
import re

PAAL_FMT    = (    '_+ow_ee_',     '_+ow_e_eT',     '_+ow_:_iyM',    '_+ow_:_owT')
NIFAL_FMT   = (  'Ni_:_@_',      'Ni_:_e_eT',     'Ni_:_@_iyM',    'Ni_:_@_owT'  )
PIEL_FMT    = (  'M:_a_+ee_',    'M:_a_+e_eT',    'M:_a_+:_iyM',   'M:_a_+:_owT' )
PUAL_FMT    = (  'M:_u_+@_',     'M:_u_+e_eT',    'M:_u_+@_iyM',   'M:_u_+@_owT' )
HITPAEL_FMT = ('MiT:_+a_+ee_', 'MiT:_+a_+e_eT', 'MiT:_+a_+:_iyM', 'MiT_+a_+:_owT')
HIFIL_FMT   = (  'Ma_:_iy_',     'Ma_:_iy_@H',    'Ma_:_iy_iyM',   'Ma_:_iy_owT' )
HUFAL_FMT   = (  'Mu_:_@_',      'Mu_:_e_eT',     'Mu_:_@_iyM',    'Mu_:_@_owT'  )

def paal_present(root, i):
    assert 0 <= i <= 3  # m.sg / f.sg / m.pl / f.pl

    fmt = PAAL_FMT[i].split('_')

    if root.e in ('A', 'H', 'H/', 'E'): # guttural(喉音)
        if i in (2, 3):
            fmt[2] = 'a:' # m.pl / f.pl
    elif root.e in ('V', 'Y'):
        # SH@R 型変化
        fmt = ('%(p)s@%(l)s', '%(p)s@%(l)s@H', '%(p)s@%(l)siyM', '%(p)s@%(l)sowT')[i]

    if root.l in ('H/', 'E'):
        # vowels[0] = '_ow_eeA_'.split('_') # m.sg, 潜入パタフ
        if i == 0:
            fmt[2] += 'A' # 潜入パタフ
        #vowels[1] = '_ow_a_aT'.split('_') # f.sg, -a-a-
        if i == 1:
            fmt[2:] = ['a', 'aT']  # vowels[1][2].replace('e', 'a')
    elif root.l == 'A':
        if i == 1:
            fmt = '=ow=ee=_T'.split('=') # f.sg, no vowels under A
    elif root.l == 'H':
        # Lamed-He
        fmt = ('%(p)sow%(e)seH', '%(p)sow%(e)s@H', '%(p)sow%(e)siyM', '%(p)sow%(e)sowT')[i]

    return root.inject(fmt)



IRREGULAR_VERBS = {
    'H L K' : {
        'inf': 'L@LeKeT',
        'imp': ('LeeK', 'L:Kiy', 'L:Kuw'),
        },
    'Y D E' : {
        'inf': 'L@DaEaT',
        },
    'N S A' : {
        'inf': 'L@SeeA_T',
        },
    'Y SH B': {
        'inf': 'L@SHeBeT',
        'imp': ('SHeeB', 'SH:Biy', 'SH:Buw'),
        },
    'Y R D' : {
        'inf': 'L@ReDeT',
        },
    'N T N' : {
        'inf': 'L@TeeT',
        'imp': ('T+eeN', 'T+:Niy', 'T+:Nuw'),
        },
    'L Q H/': {
        'inf': 'L@QaH/aT',
        'imp': ('QaH/', 'Q:H/iy', 'Q:H/uw'),
        },
}

def paal_infinitive(root):
    # if root.p in ('H', 'Y', 'N') and IRREGULAR_INF.has_key(str(root)):
    irreg = IRREGULAR_VERBS.get(str(root), None)
    if irreg and irreg.has_key('inf'):
        return irreg['inf']

    if root.p == 'A':
        fmt = 'Le_e:_o_'.split('_')
    elif root.p == 'E':
        fmt = 'La_a:_o_'.split('_')
    else:
        fmt = 'Li_:_o_'.split('_')

    if root.l == 'H':
        ## Lomed-He
        # ...oH -> ...owT
        fmt = ''.join([ fmt[0], '%(p)s', fmt[1], '%(e)s', fmt[2], 'wT' ])

    if root.e == 'V':
        ## Ein-Vav
        fmt = 'L@%(p)suw%(l)s'
    elif root.e == 'Y':
        ## Ein-Yud
        fmt = 'L@%(p)siy%(l)s'

    inf = root.inject(fmt)
#    print str(root), inf
    return inf


def paal_imperative(root, i):
    irreg = IRREGULAR_VERBS.get(str(root), None)
    if irreg and irreg.has_key('imp'):
        imp = irreg['imp']
        idx = [-1, 0, 1, -1, 2, 2][i]
#        print imp, idx
        if idx >= 0: return imp[idx]
        else: return None

    inf = paal_infinitive(root)
    return inf[2:] + [None, '', 'iy', None, 'uw', 'uw'][i]
