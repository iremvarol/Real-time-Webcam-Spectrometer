# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrometer_gui.ui'
#
# Created: Mon Mar 12 20:15:02 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(826, 561)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.figure1 = GraphicsView(self.centralwidget)
        self.figure1.setGeometry(QtCore.QRect(20, 10, 511, 181))
        self.figure1.setObjectName(_fromUtf8("figure1"))
        self.figure2 = PlotWidget(self.centralwidget)
        self.figure2.setGeometry(QtCore.QRect(20, 230, 511, 192))
        self.figure2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.figure2.setFrameShadow(QtGui.QFrame.Sunken)
        self.figure2.setObjectName(_fromUtf8("figure2"))
        self.buttonStart = QtGui.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(50, 450, 75, 41))
        self.buttonStart.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"font: 10pt \"Calibri\";"))
        self.buttonStart.setObjectName(_fromUtf8("buttonStart"))
        self.buttonStop = QtGui.QPushButton(self.centralwidget)
        self.buttonStop.setGeometry(QtCore.QRect(160, 450, 75, 41))
        self.buttonStop.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 10pt \"Calibri\";"))
        self.buttonStop.setObjectName(_fromUtf8("buttonStop"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(550, 10, 201, 411))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sliderCont = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderCont.setMaximum(255)
        self.sliderCont.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCont.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sliderCont.setTickInterval(50)
        self.sliderCont.setObjectName(_fromUtf8("sliderCont"))
        self.gridLayout.addWidget(self.sliderCont, 5, 0, 1, 1)
        self.sliderGain = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderGain.setMaximum(255)
        self.sliderGain.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGain.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sliderGain.setTickInterval(50)
        self.sliderGain.setObjectName(_fromUtf8("sliderGain"))
        self.gridLayout.addWidget(self.sliderGain, 9, 0, 1, 1)
        self.sliderExpo = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderExpo.setMinimum(1)
        self.sliderExpo.setMaximum(7)
        self.sliderExpo.setOrientation(QtCore.Qt.Horizontal)
        self.sliderExpo.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sliderExpo.setTickInterval(1)
        self.sliderExpo.setObjectName(_fromUtf8("sliderExpo"))
        self.gridLayout.addWidget(self.sliderExpo, 12, 0, 1, 1)
        self.sliderSat = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderSat.setMaximum(255)
        self.sliderSat.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSat.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sliderSat.setTickInterval(50)
        self.sliderSat.setObjectName(_fromUtf8("sliderSat"))
        self.gridLayout.addWidget(self.sliderSat, 7, 0, 1, 1)
        self.sliderWB = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderWB.setMaximum(10000)
        self.sliderWB.setSingleStep(500)
        self.sliderWB.setPageStep(1000)
        self.sliderWB.setOrientation(QtCore.Qt.Horizontal)
        self.sliderWB.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sliderWB.setTickInterval(1000)
        self.sliderWB.setObjectName(_fromUtf8("sliderWB"))
        self.gridLayout.addWidget(self.sliderWB, 14, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 13, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.sliderBright = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderBright.setMaximum(255)
        self.sliderBright.setOrientation(QtCore.Qt.Horizontal)
        self.sliderBright.setInvertedAppearance(False)
        self.sliderBright.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.sliderBright.setTickInterval(50)
        self.sliderBright.setObjectName(_fromUtf8("sliderBright"))
        self.gridLayout.addWidget(self.sliderBright, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.figure1, self.sliderGain)
        MainWindow.setTabOrder(self.sliderGain, self.buttonStart)
        MainWindow.setTabOrder(self.buttonStart, self.sliderExpo)
        MainWindow.setTabOrder(self.sliderExpo, self.figure2)
        MainWindow.setTabOrder(self.figure2, self.sliderSat)
        MainWindow.setTabOrder(self.sliderSat, self.sliderCont)
        MainWindow.setTabOrder(self.sliderCont, self.sliderBright)
        MainWindow.setTabOrder(self.sliderBright, self.buttonStop)
        MainWindow.setTabOrder(self.buttonStop, self.sliderWB)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.buttonStart.setText(_translate("MainWindow", "Start   ", None))
        self.buttonStop.setText(_translate("MainWindow", "Stop ", None))
        self.label_5.setText(_translate("MainWindow", "Exposure", None))
        self.label_6.setText(_translate("MainWindow", "White Balance", None))
        self.label.setText(_translate("MainWindow", "Brightness", None))
        self.label_3.setText(_translate("MainWindow", "Contrast", None))
        self.label_4.setText(_translate("MainWindow", "Gain", None))
        self.label_2.setText(_translate("MainWindow", "Saturation", None))

from pyqtgraph import GraphicsView, PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

