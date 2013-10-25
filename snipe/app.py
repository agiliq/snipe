#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

from snipe import res


class SnipeApp(QtGui.QWidget):

    def __init__(self):
        super(SnipeApp, self).__init__()

        self.pixmap = None
        self.initUI()

    def initUI(self):

        self.resize(1360, 760)

        hbox = QtGui.QHBoxLayout(self)
        self.pixmap = self.getScreen()
        self.pixmap = self.pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatio)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setPixmap(self.pixmap)

        hbox.addWidget(self.lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Snipe')
        self.showMaximized()

    def mousePressEvent(self, event):
        print "pressed at %s, %s" % (event.pos().x(), event.pos().y())

    def mouseReleaseEvent(self, event):
        print "released at %s, %s" % (event.pos().x(), event.pos().y())

    def mouseMoveEvent(self, event):
        print "moved at %s, %s" % (event.pos().x(), event.pos().y())

    def drawArrow(self, a, b):
        qpixmappainter = QtGui.QPainter(self.pixmap)
        arrow = QtGui.QPixmap(":/images/arrow.svg")
        qpixmappainter.drawPixmap(a, b, arrow);
        self.lbl.setPixmap(self.pixmap)

    def getScreen(self):
        return QtGui.QPixmap.grabWindow(
                    QtGui.QApplication.desktop().winId(),0,0,
                    QtGui.QApplication.desktop().screenGeometry().width(),
                    QtGui.QApplication.desktop().screenGeometry().height()
                )
