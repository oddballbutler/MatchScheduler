#!/usr/bin/env python
# -*- coding: utf-8 -*-

from challongeMatchGetter import ChallongeMatchGetter

username = "oddballbutler"
api_key = "KtLCcYrK3s8HdFTrF4IwYN8O2j8nHa2jl5WvKI4S"

match_getter = ChallongeMatchGetter(username, api_key)

match_getter.setTournament("ccr-test")

matches = match_getter.getMatches()
print(matches)
