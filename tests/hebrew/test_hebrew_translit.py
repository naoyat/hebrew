#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.translit import *
from nose.tools import eq_, ok_, with_setup

#def _wrap(s):
#   # RLM + s + LRM
#   return u'\u200F%s\u200E' % s

TEST_DATA = """
AaT+@H,אַתָּה
HiyA,הִיא
RoA_SH,רֹאשׁ
A@B,אָב
B+aYiT,בַּיִת
G+aG,גַּג
G'+aZ,גּ׳ַז
D+eLeT,דֶּלֶת
B+eGeD,בֶּגֶד
HaR,הַר
K+iT+@H,כִּתָּה
L@H+,לָהּ
G+@BoAH+,גָּבֹהַּ
D+@ViD,דָּוִד
G+uwP,גּוּף
B+owR,בֺּור
V@SHiyN:G+:TTowN,וָשִׁינְגְּטֺון
Z@H@B,זָהָב
Z'uwR:N@L,ז׳וּרְנָל
H/aG,חַג
TTowB,טֺוב
AowTTowM@TTiy,אֺוטֺומָטִי
Y@D,יָד
HiyA,הִיא
A@KaL,אָכַל
D+eReK:,דֶּרֶךְ
K+@BowD,כָּבֺוד
LeB,לֶב
MaYiM,מַיִם
N@BiyA,נָבִיא
B+eeN,בֵּן
SSuwSS,סוּס
EaL,עַל
Y@PeH,יָפֶה
SSowP,סֺוף
P+eH,פֶּה
TSeeL,צֵל
H/uwTS,חוּץ
TS'eL+ow,צ׳ֶלֺּו
QowP,קֺוף
ReGeL,רֶגֶל
SHeeN,שֵׁן
S@K@R,שָׂכָר
T+owR@H,תֺּורָה
SS@PaR,סָפַר
SSiP+eeR,סִפֵּר
SSuP+aR,סֻפַּר
SSeePeR,סֵפֶר
SSaP+@R,סַפָּר
SS:P@R,סְפָר
SSowPeeR,סֺופֵר
SSiP+uwR,סִפּוּר
SS@PuwR,סָפוּר
SSaP+iyR,סַפִּיר
B+@A,בָּא
A@B,אָב
S@R@H,שָׂרָה
YiTS:H/@Q,יִצְחָק
D+@ViD,דָּוִד
V+_MoSHeH,וּמֹשֶׁה
AaB:R@H@M,אַבְרָהָם
Y:RuwSH@LaYiM,יְרוּשָׁלַיִם
Y:RiyH/ow,יְרִיחֺו
AeGeD,אֶגֶד
QoDeSH,קֹדֶשׁ
A@BiyB,אָבִיב
A@BiyV,אָבִיו
AiM,אִם
EiM,עִם
AaL,אַל
EaL,עַל
AowR,אֺור
EowR,עֺור
A@H/,אָח
AaK:,אַךְ
K+aR,כַּר
QaR,קַר
K+oL,כֹּל
QowL,קֺול
SSaM,סַם
S@M,שָׂם
TT@E@H,טָעָה
T+@E@H,תָּעָה
TT@BaE,טָבַע
T+@BaE,תָּבַע
TTaEaM,טַעַם
TT@EaM,טָעַם
H/eReSH,חֶרֶשׁ
H/eeReeSH,חֵרֵשׁ
LaH/aSH,לַחַשׁ
L@H/aSH,לָחַשׁ
B+iyR@H,בִּירָה
B+iyR@H,בִּירָה
SSaEaD,סַעַד
SS@EaD,סָעַד
B+@KiyR,בָּכִיר
B+@HiyR,בָּהִיר
H/owRiyM,חֺורִים
HowRiyM,הֺורִים
H/iL+eeL,חִלֵּל
HiL+eeL,הִלֵּל
H/eeN,חֵן
HeeN,הֵן
L@KeM,לָכֶם
L@HeM,לָהֶם
R:H/owB,רְחֺוב
M:NaHeeL,מְנַהֵל
T+:HiL+iyM,תְּהִלִּים
HaL:Luw,הַלְלוּ
AaB:R@H@M,אַבְרָהָם
MaH/:B+eReT,מַחְבֶּרֶת
YiTS:H/@Q,יִצְחָק
M:NowR@H,מְנֺורָה
Y:L@DiyM,יְלָדִים
MeLeK:,מֶלֶךְ
AaT+:,אַתְּ
L@BaSH:T+:,לָבַשְׁתְּ
NeeP:TT:,נֵפְטְ
MiSS:K+eeN,מִסְכֵּן
MiD:B+@R,מִדְבָּר
YiSH:M:Ruw,יִשְׁמְרוּ
NiSS:G+:Ruw,נִסְגְּרוּ
YiR:M:Y@Huw,יִרְמְיָהוּ
AeQ:SS:P+owR:TT,אֶקְסְפֺּורְט
HaL:LuwY@H+,הַלְלוּיָהּ
HiN:Nuw,הִנְנוּ
D+iB+:Ruw,דִּבְּרוּ
TS:LiyL,צְלִיל
K+:NeSSeT,כְּנֶסֶת
G+:LiyD@H,גְּלִידָה
Aa:Niy,אֲנִי
Ea:BowD@H,עֲבֺודָה
TSiP+o:RiyM,צִפֳּרִים
SHiB+o:LiyM,שִׁבֳּלִים
H/o:D@SHiyM,חֳדָשִׁים
H/a:BiyL@H,חֲבִילָה
HeAe:MiyN,הֶאֱמִין
HeH/e:ZiyR,הֶחֱזִיר
HeEe:L@H,הֶעֱלָה
Ao:NiY+@H,אֳנִיָּה
B+aYiT,בַּיִת
MaL:B+eeN,מַלְבֵּן
K+aP,כַּף
MaZ:K+iyR,מַזְכִּיר
P+eH,פֶּה
MiR:P+eSSeT,מִרְפֶּסֶת
SHaB+@T,שַׁבָּת
MiL+eeA,מִלֵּא
HaSH+@MaYiM,הַשָּׁמַיִם
SSiP+uwR,סִפּוּר
P+iL:P+eeL,פִּלְפֵּל
AuL:P+@N,אֻלְפָּן
H@AuL:P+@N,הָאֻלְפָּן
EiyR,עִיר
H@EiyR,הָעִיר
H/ay,חַי
AuwLay,אוּלַי
SSiyNay,סִינַי
Aa:DoN@y,אֲדֹנָי
G+oy,גֺּוי
Aoy,אֺוי
G+@Luy,גָּלוּי
R@TSuy,רָצוּי
M@TSuy,מָצוּי
B+aN+aay,בַּנַּאי
B+:VaD+aay,בְּוַדַּאי
EiT+owNaay,עִתֺּונַאי
K+:Daay,כְּדַאי
B+@N@yv,בָּנָיו
AeH/@yv,אֶחָיו
T+aP+uwAH/,תַּפּוּחַ
M@SHiyAH/,מָשִׁיחַ
YowDeeAE,יֺודֵעַ
HiG+iyAE,הִגִּיעַ
G+@BoAH+,גָּבֹהַּ
H/@K:M@H,חָכְמָה
Q@R:B+@N,קָרְבָּן
T+@K:NiyT,תָּכְנִית
K+@L-H@A@ReTS,כָּל־הָאָרֶץ
M@H/o:R@T,מָחֳרָת
TS@Ho:RaYiM,צָהֳרַיִם
SH@R@SHiyM,שָׁרָשִׁים
Q@D@SHiyM,קָדָשִׁים
MeLeK:,מֶלֶךְ
YeLeD,יֶלֶד
SSeePeR,סֵפֶר
SSeeMeL,סֵמֶל
M:L@KiyM,מְלָכִים
SS:P@RiyM,סְפָרִים
MaH/:B+eReT,מַחְבֶּרֶת
MowLeDeT,מֺולֶדֶת
LowMeDeT,לֺומֶדֶת
M:DaB+eReT,מְדַבֶּרֶת
T+eeKeP,תֵּכֶף
B+:EeeReK:,בְּעֵרֶךְ
P+eTaH/,פֶּתַח
NeeTSaH/,נֵצַח
ZeRaE,זֶרַע
SSeLaE,סֶלַע
B+oQeR,בֹּקֶר
QoDeSH,קֹדֶשׁ
AoHeL,אֹהֶל
A@LeP,אָלֶף
D+@LeT,דָּלֶת
M@VeT,מָוֶת
P+aH/aD,פַּחַד
B+aEaL,בַּעַל
MiQ:LaH/aT,מִקְלַחַת
YowDaEaT,יֺודַעַת
QaYiTS,קַיִץ
B+aYiT,בַּיִת
ZaYiT,זַיִת
EaYiN,עַיִן
SH@MaYiM,שָׁמַיִם
Y@DaYiM,יָדַיִם
TTeLePowN,טֶלֶפֺון
AowTTowB+uwSS,אֺוטֺובּוּס
AiyN:P:LaTS:Y@H,אִינְפְלַצְיָה
AiyN:TTeN:SSiyBiy,אִינְטֶנְסִיבִי
T+eyAaTT:RowN,תֵּיאַטְרֺון
SH@LowM MaR,שָׁלֺום מַר
SH@LowM G+:BeReT,שָׁלֺום גְּבֶרֶת
B+oQeR TTowB,בֹּקֶר טֺוב
B+oQeR AowR,בֹּקֶר אֺור
EeReB TTowB,עֶרֶב טֺוב
LaY:L@H TTowB,לַיְלָה טֺוב
MaH SH+:LowM:K@,מַה שְּׁלֺומְךָ
MaH SH+:LowMeeK:,מַה שְּׁלֺומֵךְ
SH:LowMiy TTowB,שְׁלֺומִי טֺוב
T+owD@H RaB+@H,תֺּודָה רַבָּה
EaL LoA D+@B@R,עַל לֹא דָּבָר
SS:LiyH/@H,סְלִיחָה
B+:BaQ+@SH@H,בְּבַקָּשָׁה
B+@RuwK: HaB+@A,בָּרוּךְ הַבָּא
L:H/aY+iyM,לְחַיִּים
B+:TeeA@BowN,בְּתֵאָבֺון
MaZ+@L TTowB,מַזָּל טֺוב
H/aG S@MeeAH/,חַג שָׂמֵחַ
SHaB+aT SH@LowM,שַׁבַּת שָׁלֺום
LiB:RiyAuwT,לִבְרִיאוּת
B+:HaTS:L@H/@H,בְּהַצְלָחָה
L:HiT:R@AowT,לְהִתְרָאֺות
T+aL:MiyD,תַּלְמִיד
T+aL:MiyD@H,תַּלְמִידָה
A@B,אָב
D+owD,דֺּוד
MowReH,מֺורֶה
SSuwSS,סוּס
AeeM,אֵם
D+owD@H,דֺּודָה
MowR@H,מֺורָה
SSuwSS@H,סוּסָה
SSePeeR,סֶפֵר
SH@LowM,שָׁלֺום
D+iQ:D+owQ,דִּקְדֺּוק
K+iT+@H,כִּתָּה
SSaB:L@NuwT,סַבְלָנוּת
MaH/a:SH@B@H,מַחֲשָׁבָה
M:DiyN@H,מְדִינָה
AaHa:B@H,אַהֲבָה
T+owD@H,תֺּודָה
LaY:L@H,לַיְלָה
YowN@H,יֺונָה
MaH/:B+eReT,מַחְבֶּרֶת
MowLeDeT,מֺולֶדֶת
H/a:NuwT,חֲנוּת
K+aP+iyT,כַּפִּית
M@VeT,מָוֶת
SHeeRuwT,שֵׁרוּת
L@SHowN,לָשֺׁון
EaYiN,עַיִן
ReGeL,רֶגֶל
AeReTS,אֶרֶץ
EiyR,עִיר
YiS:R@AeeL,יִשְׂרָאֵל
YaP+@N,יַפָּן
Y:RuwSH@LaYiM,יְרוּשָׁלַיִם
TTowQ:Yow,טֺוקְיֺו
MoSHeH,מֹשֶׁה
MiR:Y@M,מִרְיָם
AaB:R@H@M,אַבְרָהָם
YiTS:H/@Q,יִצְחָק
YaEa:QoB,יַעֲקֹב
D+@ViD,דָּוִד
SH:LoMoH,שְׁלֹמֹה
S@R@H,שָׂרָה
RiB:Q@H,רִבְקָה
R@H/eeL,רָחֵל
H/aN+@H,חַנָּה
SHowSHaN+@H,שֺׁושַׁנָּה
H/eyP@H,חֵיפָה
T+eeL-A@BiyB,תֵּל־אָבִיב
Y:RiyH/ow,יְרִיחֺו
B+eyT-LeH/eM,בֵּית־לֶחֶם
Aa:Niy,אֲנִי
AaT+@H,אַתָּה
AaT+:,אַתְּ
HuwA,הוּא
HiyA,הִיא
Aa:NaH/:Nuw,אֲנַחְנוּ
A@Nuw,אָנוּ
AaT+eM,אַתֶּם
AaT+eN,אַתֶּן
HeeM,הֵם
HeeN,הֵן
K+eeN,כֵּן
LoA,לֹא
G+aM,גַּם
"""

test_data_table = []

def setup():
	global test_data_table
	for line in TEST_DATA.split('\n'):
		line = line.rstrip()
		if line == '': continue
		if line[0] == '#': continue ##
		lat, _heb = line.split(',')
		heb = _heb.decode('utf-8')
		test_data_table.append( (lat, heb) )

def teardown():
	pass


def _test_parse_latin_text(latin, with_vowel, expected_hebrew):
    result = parse_latin_text(latin, with_vowel)
    print u"result: u'%s'" % result,
    print u"\texpected: u'%s'" % expected_hebrew
    eq_(result, expected_hebrew)

def _test_parse_hebrew_text(hebrew, expected_latin):
    result = parse_hebrew_text(hebrew)
    if result[-1] == '_': result = result[:-1]
    print u"result: u'%s'" % result,
    print u"\texpected: u'%s'" % expected_latin
    eq_(result, expected_latin)


@with_setup(setup, teardown)
def test_parse_text():
	lats = []
	hebs = []
	for lat, heb in test_data_table:
		lats.append(lat)
		hebs.append(heb)
	latin_text = ' '.join(lats)
	hebrew_text = u' '.join(hebs)

	eq_(hebrew_text, parse_latin_text(latin_text, True))
	eq_(latin_text, parse_hebrew_text(hebrew_text))

def test_bereshit():
	latin_text = 'B+:ReeA_SHiyT, B+@R@A Ae:LoHiyM, AeeT HaSH+@MaYiM, V:AeeT H@A@ReTS.'
	hebrew_text = u'בְּרֵאשִׁית, בָּרָא אֱלֹהִים, אֵת הַשָּׁמַיִם, וְאֵת הָאָרֶץ.'

	eq_(hebrew_text, parse_latin_text(latin_text, True))
	eq_(latin_text, parse_hebrew_text(hebrew_text))


@with_setup(setup, teardown)
def test_parse_text():
	for lat, heb in test_data_table:
		_test_parse_latin_text(lat, True, heb)
		_test_parse_hebrew_text(heb, lat)
