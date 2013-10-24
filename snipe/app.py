#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class SnipeApp(QtGui.QWidget):

    def __init__(self):
        super(SnipeApp, self).__init__()

        self.initUI()

    def initUI(self):

        self.resize(1360, 760)

        hbox = QtGui.QHBoxLayout(self)
        pixmap = self.getScreen()
        pixmap = pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatio)

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Snipe')
        self.showMaximized()

    def getScreen(self):
        return QtGui.QPixmap.grabWindow(
                    QtGui.QApplication.desktop().winId(),0,0,
                    QtGui.QApplication.desktop().screenGeometry().width(),
                    QtGui.QApplication.desktop().screenGeometry().height()
                )
