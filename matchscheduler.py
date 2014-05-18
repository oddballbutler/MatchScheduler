# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject

class MatchScheduler(object):
    def __init__(self, matchGetter, matches=None):
        self.matches = matches
        self.matchGetter = matchGetter
