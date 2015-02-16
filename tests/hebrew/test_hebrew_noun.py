#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.noun import *
from nose.tools import eq_, ok_, with_setup
from tests import weak_eq_


def test_plural_form():
    def T(sg, pl):
        eq_(pl, plural_form(sg))

    T('T+aL:MiyD', 'T+aL:MiyDiyM') # 生徒(男)
    T('T+aL:MiyD@H', 'T+aL:MiyDowT') # 生徒(女)

    # 男性名詞
    T('SHiyR', 'SHiyRiyM') # 歌
    T('SSuwSS', 'SSuwSSiyM') # 馬
    T('B+@H/uwR', 'B+aH/uwRiyM') # 男子青年

    T('YeLeD', 'Y:L@DiyM') # 男児,子供
    T('SSeePeR', 'SS:P@RiyM') # 本
    T('B+eGeD', 'B+:G@DiyM') # 服
    T('MowReH', 'MowRiyM') # 先生
    T('H/owLeH', 'H/owLiyM') # 病人

    # 女性名詞
    T('H/a:BeeR@H', 'H/a:BeeRowT') # 女友達
    T('MowR@H', 'MowRowT') # 女子教員
    T('YaL:D+@H', 'Y:L@DowT') # 女の子
    T('T+:MuwN@H', 'T+:MuwNowT') # 絵,写真

    T('MaH/:B+eReT', 'MaH/:B+@RowT') # ノート
    T('RaK+eBeT', 'RaK+@BowT') # 列車
    T('TSaL+aH/aT', 'TSaL+@H/owT') # 皿

    T('K+aP+iyT', 'K+aP+iY+owT') # 小さじ
    T('M:KowNiyT', 'M:KowNiY+owT') # 自動車

    T('Z:KuwT', 'Z:KuY+owT') # 権利
    T('H/a:NuwT', 'H/a:NuY+owT') # 店


def test_affix_ha_article():
    def T(lat_without_ha, lat_with_ha):
        eq_(lat_with_ha, affix_ha_article(lat_without_ha))

    T('SSeePeR', 'HaSS+eePeR')
    T('MowR@H', 'HaM+owR@H')
    T('T+aL:MiyDiyM', 'HaT+aL:MiyDiyM')
    T('T+:MuwNowT', 'HaT+:MuwNowT')


def test_unfix_ha_article():
    def T(lat_with_ha, expected_lat_without_ha):
        is_affixed, lat_without_ha = unfix_ha_article(lat_with_ha)
        eq_(True, is_affixed)
        weak_eq_(expected_lat_without_ha, lat_without_ha)

    T('HaSS+eePeR', 'SSeePeR')
    T('HaM+owR@H', 'MowR@H')
    T('HaT+aL:MiyDiyM', 'T+aL:MiyDiyM')
    T('HaT+:MuwNowT', 'T+:MuwNowT')


def test_affix_ve():
    def T(lat_without_ve, lat_with_ve):
        weak_eq_(lat_with_ve, affix_ve(lat_without_ve))

    T('YowN@T@N', 'V:YowN@T@N')
    T('TaL:MiyDiyM', 'V:TaL:MiyDiyM')
    T('AiM+@A', 'V:AiM+@A')

    T('MoSHeH', 'UMoSHeH')
    T('B+@S@R', 'UB@S@R')
    T('P+eH', 'UPeH')
    T('T+:MuwN@H', 'UT:MuwN@H') ## dagesh removed


def test_unfix_ve():
    def T(lat_with_ve, expected_lat_without_ve):
        is_affixed, lat_without_ve = unfix_ve(lat_with_ve)
        eq_(True, is_affixed)
        weak_eq_(expected_lat_without_ve, lat_without_ve)

    T('V:YowN@T@N', 'YowN@T@N')
    T('V:TaL:MiyDiyM', 'TaL:MiyDiyM')
    T('V:AiM+@A', 'AiM+@A')

    T('UMoSHeH', 'MoSHeH')
    T('UB@S@R', 'B+@S@R')
    T('UPeH', 'P+eH')
    T('UT:MuwN@H', 'T+:MuwN@H') ## dagesh revived
