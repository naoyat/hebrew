#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.syllable import *
from hebrew.latin import cv_split, cv_unsplit
from nose.tools import eq_ #, ok_, with_setup

def test_divide_syllable():
    def T(word, expected_syllables):
        parts = cv_split(word, separate_yv=False)
        syllable_parts = divide_syllable(parts, divide_strong_dagesh=True)
        syllables = map(cv_unsplit, syllable_parts)
        def remove_last_sheva(s):
            return s[:-1] if s[-1]==':' else s
        syllables = map(remove_last_sheva, syllables)
        eq_(expected_syllables, ' - '.join(syllables))

    T('B+@A', 'B+@A')
    T('A@B', 'A@B')
    T('S@R@H', 'S@ - R@H')
    T('YiTS:H/@Q', 'YiTS - H/@Q')
    T('D+@ViD', 'D+@ - ViD')
    T('UMoSHeH', 'U - Mo - SHeH')
    T('AaB:R@H@M', 'AaB - R@ - H@M')
    T('Y:RuwSH@LaYiM', 'Y:Ruw - SH@ - La - YiM')
    T('Y:RiyH/ow', 'Y:Riy - H/ow')

    # p.25
    T('R:H/owB', 'R:H/owB')
    T('M:NaHeeL', 'M:Na - HeeL')
    ## T('T+:HiL+iyM', 'T+:Hi - L+iyM')
    T('T+:HiL+iyM', 'T+:HiL - LiyM')
    T('HaL:Luw', 'Ha - L:Luw')
    T('AaB:R@H@M', 'AaB - R@ - H@M')
    T('MaH/:B+eReT', 'MaH/ - B+e - ReT')

    # p.26
    T('M:NowR@H', 'M:Now - R@H')
    T('Y:L@DiyM', 'Y:L@ - DiyM')
    T('MeLeK', 'Me - LeK')
    T('AaT+:', 'AaT+')
    T('L@BaSH:T+:', 'L@ - BaSH:T+')
    T('NeeP:TT:', 'NeeP:TT')
    T('MiSS:K+eeN', 'MiSS - K+eeN')
    T('MiD:B+@R', 'MiD - B+@R')
    T('YiSH:M:Ruw', 'YiSH - M:Ruw')
    T('NiSS:G+:Ruw', 'NiSS - G+:Ruw')
    T('YiR:M:Y@Huw', 'YiR - M:Y@ - Huw')
    # T('AeQ:SS:P+owR:TT', 'AeQ:SS - P+owR:TT')
    T('HaL:LuwY@H+', 'Ha - L:Luw - Y@H+')
    T('HiN:Nuw', 'Hi - N:Nuw')
    ## T('D+iB+:Ruw', 'D+i - B+:Ruw')
    T('D+iB+:Ruw', 'D+iB - B:Ruw')

    # p.27
    T('TS:LiyL', 'TS:LiyL')
    T('K+:NeSSeT', 'K+:Ne - SSeT')
    T('G+:LiyD@H', 'G+:Liy - D@H')

    # 複合シェバー
    T('Aa:Niy', 'Aa:Niy')
    T('Ea:BowD@H', 'Ea:Bow - D@H')

    ## T('TSiP+o:RiyM', 'TSi - P+o:RiyM')
    T('TSiP+o:RiyM', 'TSiP - Po:RiyM')
    ## T('SHiB+o:LiyM', 'SHi - B+o:LiyM')
    T('SHiB+o:LiyM', 'SHiB - Bo:LiyM')
    T('H/o:D@SHiyM', 'H/o:D@ - SHiyM')

    # p.28
    T('H/a:BiyL@H', 'H/a:Biy - L@H')
    T('HeAe:MiyN', 'He - Ae:MiyN')
    T('HeH/e:ZiyR', 'He - H/e:ZiyR')
    T('HeEe:L@H', 'He - Ee:L@H')
    ## T('Ao:NiY+@H', 'Ao:Ni - Y+@H')
    T('Ao:NiY+@H', 'Ao:Niy - Y@H')

    T('B+aYiT', 'B+a - YiT')
    T('MaL:B+eeN', 'MaL - B+eeN')
    T('K:aP', 'K:aP')
    T('MaZ:K+iyR', 'MaZ - K+iyR')
    T('P+eH', 'P+eH')
    T('MiR:P+eSSeT', 'MiR - P+e - SSeT')

    ## T('SHaB+@T', 'SHa - B+@T')
    T('SHaB+@T', 'SHaB - B@T')
    ## T('MiL+eeA', 'Mi - L+eeA')
    T('MiL+eeA', 'MiL - LeeA')
    ## T('HaSH+@MaYiM', 'Ha - SH+@ - Ma - YiM')
    T('HaSH+@MaYiM', 'HaSH - SH@ - Ma - YiM')

    T('SSiP+uwR', 'SSiP - PuwR')
    T('P+iL:P+eeL', 'P+iL - P+eeL')

    # p.31 潜入パタフ
    ## T('T+aP+uwAH/', 'T+a - P+uwAH/')
    T('T+aP+uwAH/', 'T+aP - PuwAH/')
    T('M@SHiyAH/', 'M@ - SHiyAH/')
    T('YowDeeAE', 'Yow - DeeAE')
    ## T('HiG+iyAE', 'Hi - G+iyAE')
    T('HiG+iyAE', 'HiG - GiyAE')
    T('G+@BoAH+', 'G+@ - BoAH+')

    # p.32 カマツ・カタン
    T('H/@K:M@H', 'H/@K - M@H')
    T('Q@R:B+@N', 'Q@R - B+@N')
    T('T+@K:NiyT', 'T+@K - NiyT')
    T('H@A@ReTS', 'H@ - A@ - ReTS')

    T('M@H/o:R@T', 'M@ - H/o:R@T')
    T('TS@Ho:RaYiM', 'TS@ - Ho:Ra - YiM')
    T('SH@R@SHiyM', 'SH@ - R@ - SHiyM')
    T('Q@D@SHiyM', 'Q@ - D@ - SHiyM')

    # p.33 アクセントの位置
    T('MeLeK', 'Me - LeK')
    T('YeLeD', 'Ye - LeD')
    T('SSePeR', 'SSe - PeR')
    T('SSeeMeL', 'SSee - MeL')

    T('M:L@KiyM', 'M:L@ - KiyM')
    T('SS:P@RiyM', 'SS:P@ - RiyM')

    T('MaH/:B+eReT', 'MaH/ - B+e - ReT')
    T('MowLeDeT', 'Mow - Le - DeT')
    # p.34
    T('LowMeDeT', 'Low - Me - DeT')
    ## T('M:DaB+eReT', 'M:Da - B+e - ReT')
    T('M:DaB+eReT', 'M:DaB - Be - ReT')
    T('T+eeKeP', 'T+ee - KeP')
    T('B+:EeeReK', 'B+:Eee - ReK')

    T('P+eTaH/', 'P+e - TaH/')
    T('NeeTSaH/', 'Nee - TSaH/')
    T('ZeRaE', 'Ze - RaE')
    T('SSeLaE', 'SSe - LaE')

    T('B+oQeR', 'B+o - QeR')
    T('QoDeSH', 'Qo - DeSH')
    T('AoHeL', 'Ao - HeL')

    T('A@LeP', 'A@ - LeP')
    T('D+@LeT', 'D+@ - LeT')
    T('M@VeT', 'M@ - VeT')
    # p.35
    T('P+aH/aD', 'P+a - H/aD')
    T('B+aEaL', 'B+a - EaL')
    T('MiQ:LaH/aT', 'MiQ - La - H/aT')
    T('YowDaEaT', 'Yow - Da - EaT')

    T('QaYiTS', 'Qa - YiTS')
    T('B+aYiT', 'B+a - YiT')
    T('ZaYiT', 'Za - YiT')
    T('EaYiN', 'Ea - YiN')
    T('SH@MaYiM', 'SH@ - Ma - YiM')
    T('Y@DaYiM', 'Y@ - Da - YiM')

    T('TTeLePowN', 'TTe - Le - PowN')
    # T('AowTTowB+uwSS', 'Aow - TTow - B+uwSS')
    # T('AiyN:P:LaTS:Y@H', 'AiyN:P:La - TS:Y@H')
    T('AiyN:TTeN:SSiyBiy', 'AiyN - TTeN - SSiy - Biy')
    T('T+eyAaTT:RowN', 'T+ey - AaTT - RowN')


def test_guess_accent():
    def T(word, expected_syllables):
        parts = cv_split(word, separate_yv=False)
        syllable_parts = divide_syllable(parts, divide_strong_dagesh=True)
        accent_location = guess_accent(syllable_parts)
        syllables = map(cv_unsplit, syllable_parts)
        def remove_last_sheva(s):
            return s[:-1] if s[-1]==':' else s
        syllables = map(remove_last_sheva, syllables)
        tmp = []
        if len(syllables) == 1:
           accent_location = -1
        for i, syllable in enumerate(syllables):
            if i == accent_location:
                tmp.append('[%s]' % syllable)
            else:
                tmp.append(syllable)
        eq_(expected_syllables, ' - '.join(tmp))

    #
    # p.33 アクセントの位置
    #
    T('MeLeK', '[Me] - LeK')
    T('YeLeD', '[Ye] - LeD')
    T('SSePeR', '[SSe] - PeR')
    T('SSeeMeL', '[SSee] - MeL')

    T('M:L@KiyM', 'M:L@ - [KiyM]')
    T('SS:P@RiyM', 'SS:P@ - [RiyM]')

    T('MaH/:B+eReT', 'MaH/ - [B+e] - ReT')
    T('MowLeDeT', 'Mow - [Le] - DeT')
    # p.34
    T('LowMeDeT', 'Low - [Me] - DeT')
    ## T('M:DaB+eReT', 'M:Da - B+e - ReT')
    T('M:DaB+eReT', 'M:DaB - [Be] - ReT')
    T('T+eeKeP', '[T+ee] - KeP')
    T('B+:EeeReK', '[B+:Eee] - ReK')

    T('P+eTaH/', '[P+e] - TaH/')
    T('NeeTSaH/', '[Nee] - TSaH/')
    T('ZeRaE', '[Ze] - RaE')
    T('SSeLaE', '[SSe] - LaE')

    T('B+oQeR', '[B+o] - QeR')
    T('QoDeSH', '[Qo] - DeSH')
    T('AoHeL', '[Ao] - HeL')

    T('A@LeP', '[A@] - LeP')
    T('D+@LeT', '[D+@] - LeT')
    T('M@VeT', '[M@] - VeT')
    # p.35
    T('P+aH/aD', '[P+a] - H/aD')
    T('B+aEaL', '[B+a] - EaL')
    T('MiQ:LaH/aT', 'MiQ - [La] - H/aT')
    T('YowDaEaT', 'Yow - [Da] - EaT')

    T('QaYiTS', '[Qa] - YiTS')
    T('B+aYiT', '[B+a] - YiT')
    T('ZaYiT', '[Za] - YiT')
    T('EaYiN', '[Ea] - YiN')
    T('SH@MaYiM', 'SH@ - [Ma] - YiM')
    T('Y@DaYiM', 'Y@ - [Da] - YiM')

    # T('TTeLePowN', '[TTe] - Le - PowN')
    # T('AowTTowB+uwSS', '[Aow] - TTow - B+uwSS')
    # T('AiyN:P:LaTS:Y@H', '[AiyN:P:La] - TS:Y@H')
    # T('AiyN:TTeN:SSiyBiy', 'AiyN - TTeN - [SSiy] - Biy')
    # T('T+eyAaTT:RowN', 'T+ey - AaTT - [RowN]')

    # p.25
    T('R:H/owB', 'R:H/owB')
    T('M:NaHeeL', 'M:Na - [HeeL]')
    ## T('T+:HiL+iyM', 'T+:Hi - L+iyM')
    T('T+:HiL+iyM', 'T+:HiL - [LiyM]')
    T('HaL:Luw', 'Ha - [L:Luw]')
    T('AaB:R@H@M', 'AaB - R@ - [H@M]')
    T('MaH/:B+eReT', 'MaH/ - [B+e] - ReT')
    T('YiTS:H/@Q', 'YiTS - [H/@Q]')

    # p.26
    T('M:NowR@H', 'M:Now - [R@H]')
    T('Y:L@DiyM', 'Y:L@ - [DiyM]')
    T('MeLeK', '[Me] - LeK')
    T('AaT+:', 'AaT+')
    T('L@BaSH:T+:', 'L@ - [BaSH:T+]')
    T('NeeP:TT:', 'NeeP:TT')
    T('MiSS:K+eeN', 'MiSS - [K+eeN]')
    T('MiD:B+@R', 'MiD - [B+@R]')
    T('YiSH:M:Ruw', 'YiSH - [M:Ruw]')
    T('NiSS:G+:Ruw', 'NiSS - [G+:Ruw]')
##    T('YiR:M:Y@Huw', 'YiR - [M:Y@] - Huw')
    # T('AeQ:SS:P+owR:TT', 'AeQ:SS - P+owR:TT')
    T('HaL:LuwY@H+', 'Ha - L:Luw - [Y@H+]')
    T('HiN:Nuw', 'Hi - [N:Nuw]')
    ## T('D+iB+:Ruw', 'D+i - B+:Ruw')
    T('D+iB+:Ruw', 'D+iB - [B:Ruw]')

    # p.27
    T('TS:LiyL', 'TS:LiyL')
    T('K+:NeSSeT', '[K+:Ne] - SSeT')
##    T('G+:LiyD@H', '[G+:Liy] - D@H')

    # 複合シェバー
    T('Aa:Niy', 'Aa:Niy')
    T('Ea:BowD@H', 'Ea:Bow - [D@H]')

    ## T('TSiP+o:RiyM', 'TSi - P+o:RiyM')
    T('TSiP+o:RiyM', 'TSiP - [Po:RiyM]')
    ## T('SHiB+o:LiyM', 'SHi - B+o:LiyM')
    T('SHiB+o:LiyM', 'SHiB - [Bo:LiyM]')
    T('H/o:D@SHiyM', 'H/o:D@ - [SHiyM]')

    # p.28
    T('H/a:BiyL@H', 'H/a:Biy - [L@H]')
    T('HeAe:MiyN', 'He - [Ae:MiyN]')
    T('HeH/e:ZiyR', 'He - [H/e:ZiyR]')
    T('HeEe:L@H', 'He - [Ee:L@H]')
    ## T('Ao:NiY+@H', 'Ao:Ni - Y+@H')
    T('Ao:NiY+@H', 'Ao:Niy - [Y@H]')

    T('B+aYiT', '[B+a] - YiT')
    T('MaL:B+eeN', 'MaL - [B+eeN]')
    T('K:aP', 'K:aP')
    T('MaZ:K+iyR', 'MaZ - [K+iyR]')
    T('P+eH', 'P+eH')
    T('MiR:P+eSSeT', 'MiR - [P+e] - SSeT')

    ## T('SHaB+@T', 'SHa - B+@T')
    T('SHaB+@T', 'SHaB - [B@T]')
    ## T('MiL+eeA', 'Mi - L+eeA')
    T('MiL+eeA', 'MiL - [LeeA]')
    ## T('HaSH+@MaYiM', 'Ha - SH+@ - Ma - YiM')
    T('HaSH+@MaYiM', 'HaSH - SH@ - [Ma] - YiM')

    T('SSiP+uwR', 'SSiP - [PuwR]')
    T('P+iL:P+eeL', 'P+iL - [P+eeL]')

    # p.31 潜入パタフ
    ## T('T+aP+uwAH/', 'T+a - P+uwAH/')
    T('T+aP+uwAH/', 'T+aP - [PuwAH/]')
    T('M@SHiyAH/', 'M@ - [SHiyAH/]')
    T('YowDeeAE', 'Yow - [DeeAE]')
    ## T('HiG+iyAE', 'Hi - G+iyAE')
    T('HiG+iyAE', 'HiG - [GiyAE]')
    T('G+@BoAH+', 'G+@ - [BoAH+]')

    # p.32 カマツ・カタン
    T('H/@K:M@H', 'H/@K - [M@H]')
    T('Q@R:B+@N', 'Q@R - [B+@N]')
    T('T+@K:NiyT', 'T+@K - [NiyT]')
    T('H@A@ReTS', 'H@ - [A@] - ReTS')
    # T('K+@L-H@A@ReTS', 'K+@L H@ - [A@] - ReTS')

    T('M@H/o:R@T', 'M@ - [H/o:R@T]')
    T('TS@Ho:RaYiM', 'TS@ - [Ho:Ra] - YiM')
    T('SH@R@SHiyM', 'SH@ - R@ - [SHiyM]')
    T('Q@D@SHiyM', 'Q@ - D@ - [SHiyM]')


def test_guess_qamats_qatan():
    def T(word, expected_oa):
        result = guess_qamats_qatan(word)
        eq_(expected_oa, result)

#        syllables = map(cv_unsplit, syllable_parts)
#        accent_location = guess_qamats_qatan(syllable_parts)
#        syllables = map(cv_unsplit, syllable_parts)

    T('H/@K:M@H', 'oa')
    T('Q@R:B+@N', 'oa')
    T('T+@K:NiyT', 'o')
    T('K+@L-H@A@ReTS', 'oaa')

    T('M@H/o:R@T', 'oa')
    T('TS@Ho:RaYiM', 'o')
    T('SH@R@SHiyM', 'oa')
    T('Q@D@SHiyM', 'oa')


