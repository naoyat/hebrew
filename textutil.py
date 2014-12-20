#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

def text_trans(translator, text):
    if isinstance(text, str):
        text = text.decode('utf-8')

    buf = []
    i = 0
    while True:
        mo = re.search(ur'[ \t,.!?{}()]+', text[i:])
        if mo:
            # print "found (%s) at [%d:%d]" % (mo.group(0), i+mo.start(), i+mo.end())
            word = text[i:i+mo.start()]
            word_t = translator(word)
            buf.append(word_t)

            space = mo.group(0)
            buf.append(space)

            i += mo.end()
        else:
            # print "not found."
            word = text[i:]
            if len(word) > 0:
                word_t = translator(word)
                buf.append(word_t)
            break

    return ''.join(buf)