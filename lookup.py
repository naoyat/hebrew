#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import sys
import re

from hebrew import load_dict, lookup_text_heb, lookup_text_lat
import textutil

def flatten(stream):
    for items in stream:
        for item in items:
#            print "+", item[0]
            if isinstance(item, list) and item[0] == '#MULTI#':
                for item_ in item[1:]:
                    yield item_
            else:
                yield item

def _parse_stdin(parse_text_proc):
    while True:
        text = sys.stdin.readline()
        if not text: break
        text = text.rstrip()

        print text
        if len(text) == 0 or text[0] == '#': continue

        for item in flatten(parse_text_proc(text)):
            # if item is None: continue
#            if not isinstance(items, list): continue
            if len(item) == 5:
                print ('- %s (%s) %s' % (item[2], item[1], item[4])).encode('utf-8')
            else:
                item = re.sub(' ', '', item)
                if len(item) > 0:
                    print item
#                print '- %s ?' % (text,)
        print


@click.group()
def cli():
    load_dict()

@cli.command()
@click.option('--vowel/--no-vowel', default=False)
@click.option('--debug/--no-debug', default=False)
def latin(vowel, debug):
#    return textutil.text_trans(lookup_word_heb, text_heb, do_join=False)
    _parse_stdin(lambda text: textutil.text_trans(lookup_text_lat, text, do_join=False))

@cli.command()
def hebrew():
#    _parse_stdin(lambda text: parse_hebrew_text(text))
    _parse_stdin(lambda text: textutil.text_trans(lookup_text_heb, text, do_join=False))


if __name__ == '__main__':
    cli()
