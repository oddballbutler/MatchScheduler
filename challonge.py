# -*- coding: utf-8 -*-
import challonge

class Challonge(object):
    def __init__(self, username, api_key):
        challonge.set_credentials(username, api_key)

    def setTournament(tournament):
        self.tournament = challonge.tournaments.show(tournament)

    def getMatches():
        self.matches = challonge.matches.index(self.tournament["id"])
        return
