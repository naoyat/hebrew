#!/usr/bin/python
# -*- coding: utf-8 -*-
from hebrew.latin import cv_split, cv_unsplit

def divide_syllable(parts, divide_strong_dagesh=False):
    seps = [ None ] * len(parts)
    last = len(parts) - 1

    i = 0
    while i <= last:
        part = parts[i]
        if part[0] == '-':
            seps[i] = True
        elif part[0] == 'V+':
            seps[i] = True
        elif part[1] == None:
            if i > 0: seps[i-1] = False
        elif part[1] in ('a:', 'e:', 'o:'):
            seps[i] = False
            if i > 0: seps[i-1] = True
        elif part[1] in (':', 'a:', 'e:', 'o:'):
            if i == 0:
                seps[i] = False
            elif i == last:
                if i > 0: seps[i-1] = False
            elif part[0][-1] == '+':
                # 強ダゲッシュの下に来るシェバーは有音
                seps[i] = False
                if i > 0: seps[i-1] = True
            else:
                seps[i] = True
                if i > 0: seps[i-1] = False

            # ２連シェバー
            if i+i <= last and parts[i+1][1] == ':': # in (':', 'a:', 'e:', 'o:'):
                if i+1 < last:
                    seps[i] = True
                else:
                    seps[i] = False
                i += 1

            # 同じ子音
            if i+i <= last and part[0] == parts[i+1][0]:
                if i > 0: seps[i-1] = True
                seps[i] = False
        else:
            # pass
            seps[i] = True
        i += 1

    syllables = []
    stack = []
    for part, sep in zip(parts, seps):
        stack.append(part)
        if sep:
            syllables.append(stack)
            stack = []
    if stack:
        syllables.append(stack)

    if divide_strong_dagesh:
        for i, parts in enumerate(syllables):
            if i == len(syllables)-1:
                if parts[-1] == ['H+', 'a']: break
            if i > 0 and parts[0][0][-1] == '+' and syllables[i-1][-1][1] != ':':
                syllables[i-1].append( (parts[0][0][:-1], None) )
                syllables[i][0][0] = syllables[i][0][0][:-1]

    # 潜入パタフ
    if len(syllables) >= 2:
        last_syllable = syllables[-1]
        if last_syllable[-1][1] == 'a' and last_syllable[-1][0] in ('H+', 'H/', 'E'):
            syllables = syllables[:-1]
            syllables[-1] += last_syllable

    return syllables


def guess_accent(syllable_parts):
    ultima = len(syllable_parts)-1

    if len(syllable_parts) == 1:
        return 0

    if len(syllable_parts) >= 2:
        first = syllable_parts[-2]
        second = syllable_parts[-1]
        if len(first) >= 1 and len(second) == 2:
            if first[-1][1] in ('e', 'ee') and second[0][1] == 'e':
                # セゴリーム （ミルエル）
                return ultima - 1
            if first[-1][1] in ('e', 'ee') and second[0][1] == 'a' and second[-1][0] in ('H/', 'E'):
                # セゴリーム （ミルエル）
                return ultima - 1
            if first[-1][1] == 'o' and second[0][1] == 'e':
                if syllable_parts == [[['M', 'o']], [['SH', 'e'], ['H', None]]]:
                    return ultima # MoSHeH
                else:
                    return ultima - 1
            if first[-1][1] == '@' and second[0][1] == 'e':
                return ultima - 1
            if first[-1][1] == 'a' and second[0][1] == 'a' and second[0][0] in ('H/', 'E'):
                return ultima - 1
            if first[-1][1] == 'a' and second[0] == ['Y', 'i']:
                return ultima - 1

    return ultima

def guess_qamats_qatan(word):
    if word in ('SH@R@SHiyM', 'Q@D@SHiyM'):
        return 'oa'

    parts = cv_split(word, separate_yv=False)
    syllable_parts = divide_syllable(parts, divide_strong_dagesh=True)
    # print syllable_parts

    accent_location = guess_accent(syllable_parts)

    tmp = []
    for i, parts in enumerate(syllable_parts):
        accented = (i == accent_location)
        qq_at = 0
        if parts[0][1] != '@':
            qq_at = 1
            if parts[0][1] == 'o:':
                if len(tmp) > 0: tmp[-1] = 'o'
            if len(parts) == 1 or parts[1][1] != '@': continue
        # print "P", parts, qq_at

        if parts == [['K+', '@'], ['L', None], ['-', None]]: # 連語形の kol-
            tmp.append('o')
            continue
        elif accented or len(parts) == 1:
            tmp.append('a')
            continue
        elif len(parts) >= (qq_at+2) and parts[qq_at+1][1] == ':':
            tmp.append('o')
            continue
        tmp.append('a')

    return ''.join(tmp)
