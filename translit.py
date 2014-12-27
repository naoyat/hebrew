#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import sys

from hebrew.translit import parse_latin_text, parse_hebrew_text

def _parse_stdin(parse_text_proc):
    while True:
        text = sys.stdin.readline()
        if not text: break
        text = text.rstrip()
        # print text
        print parse_text_proc(text).encode('utf-8')


@click.group()
def cli():
    pass

@cli.command()
@click.option('--vowel/--no-vowel', default=False)
@click.option('--debug/--no-debug', default=False)
def latin(vowel, debug):
    _parse_stdin(lambda text: parse_latin_text(text, vowel, debug))

@cli.command()
def hebrew():
    _parse_stdin(lambda text: parse_hebrew_text(text))


if __name__ == '__main__':
    cli()