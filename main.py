#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from matchscheduler import MatchScheduler
from challongeMatchGetter import ChallongeMatchGetter
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QStringListModel

def main():
    match_getter = ChallongeMatchGetter("oddballbutler", "KtLCcYrK3s8HdFTrF4IwYN8O2j8nHa2jl5WvKI4S")
    match_getter.setTournament("ccr-test")
    scheduler = MatchScheduler(match_getter)
    app = QApplication(sys.argv)

    scheduler.updateMatches()
    matches = scheduler.getScheduledMatches()

    myStringList = []

    for x in matches:
        myStringList.append(x.__str__())

    myListModel = QStringListModel(myStringList)

    window = uic.loadUi("mainwindow.ui")
    window.listView.setModel(myListModel)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
