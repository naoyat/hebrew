#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.verb import *
from hebrew.root import Root
from nose.tools import eq_, ok_, with_setup
from tests import weak_eq_
#from hebrew.translit import parse_latin_word


def test_paal():
    def T_present(root, expected_present_forms):
        for i in range(4):
            result = paal_present(root, i)
            expected = expected_present_forms[i]
            if expected:
                weak_eq_(expected, result)
    def T_present1(root, expected_present_forms):
        result = paal_present(root, 0)
        expected = expected_present_forms[0]
        weak_eq_(expected, result)

    def T_infinitive(root, expected_inf_form):
        result = paal_infinitive(root)
        weak_eq_(expected_inf_form, result)

    def T_imperative(root, expected_imperative_forms):
        pers2_sg_m  = paal_imperative(root, 1)
        pers2_sg_f  = paal_imperative(root, 2)
        pers2_pl_mf = paal_imperative(root, 4)
        weak_eq_(expected_imperative_forms[0], pers2_sg_m)
        weak_eq_(expected_imperative_forms[1], pers2_sg_f)
        weak_eq_(expected_imperative_forms[2], pers2_pl_mf)

    # L-M-D 学ぶ
    root = Root('LMD')
    T_present(root, ['LowMeeD', 'LowMeDeT', 'LowM:DiyM', 'LowM:DowT'])
    T_infinitive(root, 'LiL:MoD')

    # K-T-B 書くKT
    root = Root('KTB')
    T_present(root, ['K+owTeeB', 'K+owTeBeT', 'K+owT:BiyM', 'K+owT:BowT'])
    T_infinitive(root, 'LiK:T+oB')

    # G-M-R 終える
    root = Root('GMR')
    T_present(root, ['G+owMeeR', 'G+owMeReT', 'G+owM:RiyM', 'G+owM:RowT'])
    T_infinitive(root, 'LiG:MoR')

    # L-B-SH 着る
    root = Root('L B SH')
    T_present(root, ['LowBeeSH', 'LowBeSHeT', 'LowB:SHiyM', 'LowB:SHowT'])
    T_infinitive(root, 'LiL:B+oSH')

    # A-K-L 食べる
    root = Root('AKL')
    T_present(root, ['AowKeeL', 'AowKeLeT', 'AowK:LiyM', 'AowK:LowT'])
    T_infinitive(root, 'LeAe:KoL')

    # H-L-K 行く
    root = Root('HLK')
    T_present(root, ['HowLeeK', 'HowLeKeT', 'HowL:KiyM', 'HowL:KowT'])
    T_infinitive(root, 'L@LeKeT')
    T_imperative(root, ['LeeK', 'L:Kiy', 'L:Kuw'])

    # SH-M-R 守る
    root = Root('SH M R')
    T_present(root, ['SHowMeeR', 'SHowMeReT', 'SHowM:RiyM', 'SHowM:RowT'])
    T_infinitive(root, 'LiSH:MoR')

    # P-G-SH 会う
    root = Root('P G SH')
    T_present(root, ['P+owGeeSH', 'P+owGeSHeT', 'P+owG:SHiyM', 'P+owG:SHowT'])
    T_infinitive(root, 'LiP:G+oSH')

    # SS-G-R 閉める
    root = Root('SS G R')
    T_present(root, ['SSowGeeR', 'SSowGeReT', 'SSowG:RiyM', 'SSowG:RowT'])
    T_infinitive(root, 'LiSS:G+oR')
#    T_imperative(root, ['SS:GoR', 'SSiG:Riy', 'SSiG:Ruw'])

    # A-M-R 言う
    root = Root('AMR')
    T_present(root, ['AowMeeR', 'AowMeReT', 'AowM:RiyM', 'AowM:RowT'])

    # E-M-D 立つ
    root = Root('EMD')
    T_infinitive(root, 'LaEa:MoD')

    # E-B-D 働く
    root = Root('EBD')
    T_infinitive(root, 'LaEa:BoD')

    # H/-SH-B 考える,思う
    root = Root('H/ SH B')
    T_present1(root, ['H/owSHeeB'])


    # M-SS-R 伝える
    root = Root('M SS R')
    T_present1(root, ['MowSSeeR'])

    # Z-K-R 覚えている
    root = Root('ZKR')
    T_present1(root, ['ZowKeeR'])

    ## 語根に喉音がある場合

    # SH-(A)-L 質問する
    root = Root('SH A L')
    T_present(root, ['SHowAeeL', 'SHowAeLeT', 'SHowAa:LiyM', 'SHowAa:LowT'])

    # L-Q-(H/) 取る
    root = Root('L Q H/')
    T_present(root, ['LowQeeAH/', 'LowQaH/aT', 'LowQ:H/iyM', 'LowQ:H/owT'])
    T_infinitive(root, 'L@QaH/aT') ## 不規則！

    # SH-M-(E) 聞く
    root = Root('SH M E')
    T_present(root, ['SHowMeeAE', 'SHowMaEaT', 'SHowM:EiyM', 'SHowM:EowT'])

    # Q-R-(A) 読む
    root = Root('QRA')
    T_present(root, ['QowReeA', 'QowReeA_T', 'QowR:AiyM', 'QowR:AowT'])

    # B-H/-R 選ぶ
    root = Root('B H/ R')
    T_present(root, ['B+owH/eeR', 'B+owH/eReT', 'B+owH/a:RiyM', 'B+owH/a:RowT'])

    # A-H-B 愛する,好む
    root = Root('AHB')
    T_present1(root, ['AowHeeB'])
    T_infinitive(root, 'LeAe:HoB')

    # K-E-SS 怒る
    root = Root('K E SS')
    T_present1(root, ['K+owEeeSS'])

    # R-H/-TS 愛する
    root = Root('R H/ TS')
    T_infinitive(root, 'LiR:H/oTS')

    # E-TS-R 止まる
    root = Root('E TS R') # E@TSaR
#    T_imperative(root, ['Ea:TSoR', None, None])

    # SH-L-(H/) 送る
    root = Root('SH L H/')
    T_present1(root, ['SHowLeeAH/'])

    # N-SS-(E) 行く
    root = Root('N SS E')
    T_present1(root, ['NowSSeeAE'])

    # P-T-(H/) 開く
    root = Root('P T H/')
    T_present1(root, ['P+owTeeAH/'])

    # Y-D-(E) 知る
    root = Root('YDE')
    T_present1(root, ['YowDeeAE'])
    #T_infinitive(root, 'L@DaEaT')

    # B-R-(H/) 逃げる
    root = Root('B R H/')
    T_present1(root, ['B+owReeAH/'])

    # M-TS-(A) 見つける
    root = Root('M TS A')
    T_present1(root, ['MowTSeeA'])

    # Y-TS-(A) 出る
    root = Root('Y TS A')
    T_present1(root, ['YowTSeeA'])


    ## Lamed-He

    # R-TS-(H) 欲する
    root = Root('R TS H')
    T_present(root, ['RowTSeH', 'RowTS@H', 'RowTSiyM', 'RowTSowT'])

    # Q-N-(H) 買う
    root = Root('QNH')
    T_present(root, ['QowNeH', 'QowN@H', 'QowNiyM', 'QowNowT'])
    T_infinitive(root, 'LiQ:NowT')

    # B-N-(H) 建てる
    root = Root('BNH')
    T_present(root, ['BowNeH', 'BowN@H', 'BowNiyM', 'BowNowT'])
    T_infinitive(root, 'LiB:NowT')

    # P-N-(H) 曲がる
    root = Root('PNH')
    T_present(root, ['PowNeH', 'PowN@H', 'PowNiyM', 'PowNowT'])
    T_infinitive(root, 'LiP:NowT')

    # E-N-(H) 答える
    root = Root('ENH')
    T_present(root, ['EowNeH', 'EowN@H', 'EowNiyM', 'EowNowT'])
    T_infinitive(root, 'LaEa:NowT')

    # E-L-(H) 上がる
    root = Root('ELH')
    T_present(root, ['EowLeH', 'EowL@H', 'EowLiyM', 'EowLowT'])
    T_infinitive(root, 'LaEa:LowT')

    # R-A-(H) 見る,分かる
    root = Root('RAH')
    T_present(root, ['RowAeH', 'RowA@H', 'RowAiyM', 'RowAowT'])
    T_infinitive(root, 'LiR:AowT')

    # E-S-(H) する,作る
    root = Root('ESH')
    T_present(root, ['EowSeH', 'EowS@H', 'EowSiyM', 'EowSowT'])
    T_infinitive(root, 'LaEa:SowT')


    # B-K-(H) 泣く
    root = Root('BKH')
    T_infinitive(root, 'LiB:K+owT')

    # SH-T-(H)
    root = Root('SH T H')
    T_infinitive(root, 'LiSH:T+owT')

    # S-H/-(H) 泳ぐ
    root = Root('S H/ H')
    T_infinitive(root, 'LiS:H/owT')

    # SH-T-(H) 飲む
    root = Root('SH T H')
    T_infinitive(root, 'LiSH:T+owT')


    ## Ein-Vav, Ein-Yud

    # Q-(V)-M 起きる
    root = Root('QVM')
    T_present(root, ['Q@M', 'Q@M@H', 'Q@MiyM', 'Q@MowT'])
    T_infinitive(root, 'L@QuwM')
    T_imperative(root, ['QuwM', 'QuwMiy', 'QuwMuw'])

    # G-(V)-R 住む
    root = Root('GVR')
    T_present(root, ['G+@R', 'G+@R@H', 'G+@RiyM', 'G+@RowT'])
    T_infinitive(root, 'L@GuwR')

    # B-(V)-A
    root = Root('BVA')
    T_infinitive(root, 'L@BowA')
    T_imperative(root, ['B+owA', 'B+owAiy', 'B+owAuw'])

    # S-(Y)-M 気をつける？
    root = Root('SYM')
    T_infinitive(root, 'L@SiyM')
    T_imperative(root, ['SiyM', 'SiyMiy', 'SiyMuw'])


    # SH-(Y)-R 歌う
    root = Root('SH Y R')
    T_present(root, ['SH@R', 'SH@R@H', 'SH@RiyM', 'SH@RowT'])
    T_infinitive(root, 'L@SHiyR')

    # R * TS 走る
    #T_present(root, ['R@TS', 'R@TS@H', 'R@TSiyM', 'R@TSowT'])
    # N * H/ 休む
    #T_present(root, ['N@H/', 'N@H/@H', 'N@H/iyM', 'N@H/owT'])
    # B * A 来る
    #T_present(root, ['B+@A', 'B+@A@H', 'B+@AiyM', 'B+@AowT'])
    # S * M 置く
    #T_present(root, ['S@M', 'S@M@H', 'S@MiyM', 'S@MowT'])


    ## irregular

    # (H)-L-K 歩く
    root = Root('HLK')
    T_infinitive(root, 'L@LeKeT')

    # (N)-S-A 上げる
    root = Root('NSA')
    T_infinitive(root, 'L@SeeA_T')

    # (Y)-SH-B 座る
    root = Root('Y SH B')
    T_infinitive(root, 'L@SHeBeT')
    T_imperative(root, ['SHeeB', 'SH:Biy', 'SH:Buw'])

    # (Y)-R-D 降りる
    root = Root('YRD')
    T_infinitive(root, 'L@ReDeT')

    # (N)-T-N 与える
    root = Root('NTN')
    T_infinitive(root, 'L@TeeT')
    T_imperative(root, ['T+eeN', 'T+:Niy', 'T+:Nuw'])

    # L-Q-H/ 取る
    root = Root('L Q H/')
    T_infinitive(root, 'L@QaH/aT')
