# -*- coding: utf-8 -*-
from operator import attrgetter

class MatchScheduler(object):
    def __init__(self, match_getter, matches=None):
        self.matches = matches
        self.matchGetter = match_getter
        self.matchAttributePriorityList = ('identifier')

    def getScheduledMatches(self):
        s = sorted(self.matches, key=attrgetter(self.matchAttributePriorityList))
        return s

    def updateMatches(self):
        self.matches = self.matchGetter.getMatches()


class Match(object):
    def __init__(self, identifier, participants, round=None):
        self.identifier = identifier
        self.participants = participants
        self.round = round

    def __repr__(self):
        return str({'identifier':self.identifier, 'participants':self.participants, 'round':self.round})

    def __str__(self):
        return str({'identifier':self.identifier, 'participants':self.participants, 'round':self.round})
