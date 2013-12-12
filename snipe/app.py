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

        self.resize(1360, 768)

        hbox = QtGui.QVBoxLayout(self)
        self.pixmap = self.getScreen()
        self.pixmap = self.pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatio)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setMinimumSize(240, 160)

        hbox.addWidget(self.lbl)
        self.setLayout(hbox)

        self.createButtonsLayout()
        hbox.addLayout(self.buttonsLayout)

        self.move(300, 200)
        self.setWindowTitle('Snipe')
        self.showMaximized()

    def saveScreenshot(self):
        format = 'png'
        initialPath = QtCore.QDir.currentPath() + "/untitled." + format

        fileName = QtGui.QFileDialog.getSaveFileName(self, "Save As",
                initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        if fileName:
            self.pixmap.save(fileName, format)

    def createButtonsLayout(self):
        self.saveScreenshotButton = self.createButton("Save Screenshot",
                self.saveScreenshot)

        self.quitScreenshotButton = self.createButton("Quit", self.close)

        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.saveScreenshotButton)
        self.buttonsLayout.addWidget(self.quitScreenshotButton)

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button
    def mousePressEvent(self, event):
        self.arrowStart = event.pos()
        print "pressed at %s, %s" % (event.pos().x(), event.pos().y())

    def mouseReleaseEvent(self, event):
        self.arrowEnd = event.pos()
        line = QtCore.QLineF(self.arrowStart, self.arrowEnd)
        self.drawArrow(line)
        text, ok = QtGui.QInputDialog.getText(self, 'Text',
            'Enter text:')

        if ok:
            text = str(text)
            qp = QtGui.QPainter(self.pixmap)
            qp.setPen(QtCore.Qt.red)
            qp.setFont(QtGui.QFont('Sans', 30))
            dest = QtCore.QRectF(line.p2(), QtCore.QPointF(line.p2().x()+100, line.p2().y()+100))
            qp.drawText(dest, QtCore.Qt.AlignCenter, text)
            self.lbl.setPixmap(self.pixmap)
        print "released at %s, %s" % (event.pos().x(), event.pos().y())


    def mouseMoveEvent(self, event):
        print "moved at %s, %s" % (event.pos().x(), event.pos().y())

    def drawArrow(self, line):
        qp = QtGui.QPainter(self.pixmap)
        arrow = QtGui.QPixmap(":/images/arrow.svg")
        rotate = QtGui.QTransform()
        rotate.rotate(-line.angle())
        arrow = arrow.transformed(rotate)
        source = QtCore.QRectF(0, 0, arrow.width(), arrow.height())
        dest = QtCore.QRectF(line.p1(), line.p2())
        qp.drawPixmap(dest, arrow, source);
        self.lbl.setPixmap(self.pixmap)

    def getScreen(self):
        return QtGui.QPixmap.grabWindow(
                    QtGui.QApplication.desktop().winId(),0,0,
                    QtGui.QApplication.desktop().screenGeometry().width(),
                    QtGui.QApplication.desktop().screenGeometry().height()
                )
