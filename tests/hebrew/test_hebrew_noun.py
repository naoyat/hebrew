#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.noun import *
from nose.tools import eq_, ok_, with_setup


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


def test_ha_article():
    def T(lat_without_ha, lat_with_ha):
        eq_(lat_with_ha, ha_article(lat_without_ha))

    T('SSeePeR', 'HaSS+eePeR')
    T('MowR@H', 'HaM+owR@H')
    T('T+aL:MiyDiyM', 'HaT+aL:MiyDiyM')
    T('T+:MuwNowT', 'HaT+:MuwNowT')


def test_with_ve():
    def T(lat_without_ve, lat_with_ve):
        eq_(lat_with_ve, with_ve(lat_without_ve))

    T('YowN@T@N', 'V:YowN@T@N')
    T('TaL:MiyDiyM', 'V:TaL:MiyDiyM')
    T('AiM+@A', 'V:AiM+@A')

    T('MoSHeH', 'V+_MoSHeH')
    T('B@S@R', 'V+_B@S@R')
    T('P+eH', 'V+_PeH')
    T('T+:MuwN@H', 'V+_T:MuwN@H')
