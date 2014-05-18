# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtProperty

class Match(object):

    def __init__(self, id, participants):
        self.id = id
        self.participants = participants
