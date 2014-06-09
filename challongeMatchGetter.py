# -*- coding: utf-8 -*-
import challonge
from match import Match

class ChallongeMatchGetter(object):
    def __init__(self, username, api_key):
        challonge.set_credentials(username, api_key)

    def setTournament(self, tournament):
        self.tournament = challonge.tournaments.show(tournament)

    def getMatches(self):
        self.matches = []
        challongeMatches = challonge.matches.index(self.tournament["id"], state="open")
        for match in challongeMatches:
            player1 = challonge.participants.show(self.tournament["id"], match["player1-id"])
            player2 = challonge.participants.show(self.tournament["id"], match["player2-id"])
            participants = [player1["name"],player2["name"]]
            self.matches.append(Match(match["id"],participants))

        return self.matches
