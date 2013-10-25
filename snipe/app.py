#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

from snipe import res

ARROW_WIDTH = 100


class SnipeApp(QtGui.QWidget):

    def __init__(self):
        super(SnipeApp, self).__init__()

        self.pixmap = None
        self.arrowStart = self.arrowEnd = 0
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
        self.arrowStart = event.pos()
        print "pressed at %s, %s" % (event.pos().x(), event.pos().y())

    def mouseReleaseEvent(self, event):
        self.arrowEnd = event.pos()
        line = QtCore.QLineF(self.arrowStart, self.arrowEnd)
        self.drawArrow(line)
        print "released at %s, %s" % (event.pos().x(), event.pos().y())

    def mouseMoveEvent(self, event):
        print "moved at %s, %s" % (event.pos().x(), event.pos().y())

    def drawArrow(self, line):
        qpixmappainter = QtGui.QPainter(self.pixmap)
        arrow = QtGui.QPixmap(":/images/arrow.svg")
        rotate = QtGui.QTransform()
        rotate.rotate(-line.angle())
        arrow = arrow.transformed(rotate)
        source = QtCore.QRectF(0, 0, arrow.width(), arrow.height())
        dest = QtCore.QRectF(line.p1(), line.p2())
        qpixmappainter.drawPixmap(dest, arrow, source);
        self.lbl.setPixmap(self.pixmap)

    def getScreen(self):
        return QtGui.QPixmap.grabWindow(
                    QtGui.QApplication.desktop().winId(),0,0,
                    QtGui.QApplication.desktop().screenGeometry().width(),
                    QtGui.QApplication.desktop().screenGeometry().height()
                )
