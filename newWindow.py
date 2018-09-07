from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewWindow(object):

    def setupUi(self, NewWindow):

        NewWindow.setObjectName("NewWindow")
        NewWindow.resize(591, 346)

        self.Heading = QtWidgets.QLabel(NewWindow)
        self.Heading.setGeometry(QtCore.QRect(220, 130, 147, 19))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")

        self.name_box = QtWidgets.QLineEdit(NewWindow)
        self.name_box.setGeometry(QtCore.QRect(125, 170, 331, 31))
        self.name_box.setObjectName("name_box")

        self.pushButton = QtWidgets.QPushButton(NewWindow)
        self.pushButton.setGeometry(QtCore.QRect(260, 220, 75, 27))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.retranslateUi(NewWindow)
        QtCore.QMetaObject.connectSlotsByName(NewWindow)

    def retranslateUi(self, NewWindow):
        _translate = QtCore.QCoreApplication.translate
        NewWindow.setWindowTitle(_translate("NewWindow", "New"))
        self.Heading.setText(_translate("NewWindow", "Enter New Team Name"))
        self.pushButton.setText(_translate("NewWindow", "Create"))
