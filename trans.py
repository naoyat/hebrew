#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import sys

from hebrew.translit import parse_latin_text, parse_hebrew_text

@click.group()
#@click.pass_context
def cli(): # ctx, vowel):
    # ctx.obj['vowel'] = vowel
    pass


@cli.command()
@click.option('--vowel/--no-vowel', default=False)
@click.option('--debug/--no-debug', default=False)
# @click.pass_context
# def latin(ctx):
def latin(vowel, debug):
    while True:
        text = sys.stdin.readline()
        if not text: break
        text = text.rstrip()
        # print text
        print parse_latin_text(text, vowel, debug).encode('utf-8')


@cli.command()
# @click.pass_context
def hebrew():
    while True:
        text = sys.stdin.readline()
        if not text: break
        text = text.rstrip()
        # print text
        print parse_hebrew_text(text).encode('utf-8')


if __name__ == '__main__':
    cli()