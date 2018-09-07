from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OpenWindow(object):

    def setupUi(self, OpenWindow):

        OpenWindow.setObjectName("OpenWindow")
        OpenWindow.resize(591, 346)
        
        self.openHeading = QtWidgets.QLabel(OpenWindow)
        self.openHeading.setGeometry(QtCore.QRect(240, 130, 114, 19))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.openHeading.setFont(font)
        self.openHeading.setObjectName("openHeading")

        self.openName_box = QtWidgets.QLineEdit(OpenWindow)
        self.openName_box.setGeometry(QtCore.QRect(125, 170, 331, 31))
        self.openName_box.setObjectName("openName_box")

        self.openButton = QtWidgets.QPushButton(OpenWindow)
        self.openButton.setGeometry(QtCore.QRect(260, 220, 75, 27))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")

        self.retranslateUi(OpenWindow)
        QtCore.QMetaObject.connectSlotsByName(OpenWindow)

    def retranslateUi(self, OpenWindow):
        _translate = QtCore.QCoreApplication.translate
        OpenWindow.setWindowTitle(_translate("OpenWindow", "Open"))
        self.openHeading.setText(_translate("OpenWindow", "Enter Team Name"))
        self.openButton.setText(_translate("OpenWindow", "Open"))
