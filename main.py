#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = uic.loadUi("mainwindow.ui")
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
