#!/usr/bin/python
# -*- coding: utf-8 -*-

class Root:
    def __init__(self, letters):
        if isinstance(letters, str):
            if len(letters) != 3:
                self.letters = letters.split(' ')
            else:
                self.letters = letters
        else:
            self.letters = letters

        self.p = self.letters[0]
        self.e = self.letters[1]
        self.l = self.letters[2]
        self.pel = {'p':self.p, 'e':self.e, 'l':self.l}

    def __getitem__(self, i):
        assert 0 <= i <= 2
        return self.letters[i]

    def __repr__(self):
        return '%(p)s %(e)s %(l)s' % self.pel

    def inject(self, fmt, delim='_'):
        if isinstance(fmt, str):
            if '%(' in fmt:
                return fmt % self.pel
            else:
                fmt = fmt.split(delim)
        elif not isinstance(fmt, list):
            return None
        return ''.join([ fmt[0], self.p, fmt[1], self.e, fmt[2], self.l, fmt[3] ])
