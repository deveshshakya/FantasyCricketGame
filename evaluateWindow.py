import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EvaluateWindow(object):

    def setupUi(self, EvaluateWindow):

        EvaluateWindow.setObjectName("EvaluateWindow")
        EvaluateWindow.resize(750, 574)

        self.centralwidget = QtWidgets.QWidget(EvaluateWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Evaluate_heading = QtWidgets.QLabel(self.centralwidget)
        self.Evaluate_heading.setGeometry(QtCore.QRect(200, 30, 340, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.Evaluate_heading.setFont(font)
        self.Evaluate_heading.setObjectName("Evaluate_heading")

        self.TeamName_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.TeamName_dropdown.setGeometry(QtCore.QRect(70, 80, 171, 22))
        self.TeamName_dropdown.setObjectName("TeamName_dropdown")

        # TeamNames
        Teams = sqlite3.connect("TEAM.db")
        cursor = Teams.cursor()
        cursor.execute("SELECT DISTINCT team_name FROM teams")
        teamNames = cursor.fetchall()
        Teams.close()

        # Adding names in TeamName_dropdown
        self.TeamName_dropdown.clear()
        teamNames = [a[0] for a in teamNames]
        teamNames.insert(0, 'Select Team')
        self.TeamName_dropdown.addItems(teamNames)

        self.MatchName_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.MatchName_dropdown.setGeometry(QtCore.QRect(508, 80, 171, 22))
        self.MatchName_dropdown.setObjectName("MatchName_dropdown")

        # Default Match Added
        self.MatchName_dropdown.addItem('Select Match')
        self.MatchName_dropdown.addItem('Match 1')

        self.Seprator = QtWidgets.QFrame(self.centralwidget)
        self.Seprator.setGeometry(QtCore.QRect(37, 120, 671, 20))
        self.Seprator.setFrameShape(QtWidgets.QFrame.HLine)
        self.Seprator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Seprator.setObjectName("Seprator")

        self.Players_list = QtWidgets.QListWidget(self.centralwidget)
        self.Players_list.setGeometry(QtCore.QRect(60, 180, 256, 301))
        self.Players_list.setObjectName("Players_list")

        self.Points_list = QtWidgets.QListWidget(self.centralwidget)
        self.Points_list.setGeometry(QtCore.QRect(440, 180, 256, 301))
        self.Points_list.setObjectName("Points_list")

        self.Players_head = QtWidgets.QLabel(self.centralwidget)
        self.Players_head.setGeometry(QtCore.QRect(70, 150, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Players_head.setFont(font)
        self.Players_head.setObjectName("Players_head")

        self.Points_head = QtWidgets.QLabel(self.centralwidget)
        self.Points_head.setGeometry(QtCore.QRect(450, 150, 36, 18))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Points_head.setFont(font)
        self.Points_head.setObjectName("Points_head")

        self.Points = QtWidgets.QLabel(self.centralwidget)
        self.Points.setGeometry(QtCore.QRect(510, 150, 41, 18))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Points.setFont(font)
        self.Points.setObjectName("Points")

        self.Calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate_button.setGeometry(QtCore.QRect(320, 510, 111, 26))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Calculate_button.setFont(font)
        self.Calculate_button.setObjectName("Calculate_button")
        EvaluateWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EvaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(EvaluateWindow)

    def retranslateUi(self, EvaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        EvaluateWindow.setWindowTitle(_translate("EvaluateWindow", "Evaluate"))
        self.Evaluate_heading.setText(_translate("EvaluateWindow", "Evaluate the Performance Of Your Fantasy Team"))
        self.Players_head.setText(_translate("EvaluateWindow", "Players"))
        self.Points_head.setText(_translate("EvaluateWindow", "Points"))
        self.Points.setText(_translate("EvaluateWindow", "00"))
        self.Calculate_button.setText(_translate("EvaluateWindow", "Calculate Score"))
