# -*- coding: utf-8 -*-

class MatchScheduler(object):
    def __init__(self, matchGetter, matches=None):
        self.matches = matches
        self.matchGetter = matchGetter
