import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from newWindow import Ui_NewWindow
from openWindow import Ui_OpenWindow
from evaluateWindow import Ui_EvaluateWindow


class Ui_MainWindow(object):

    def __init__(self):
        self.newDialog = QtWidgets.QMainWindow()
        self.newScreen = Ui_NewWindow()
        self.newScreen.setupUi(self.newDialog)

        self.openDialog = QtWidgets.QMainWindow()
        self.openScreen = Ui_OpenWindow()
        self.openScreen.setupUi(self.openDialog)

        self.evaluateDialog = QtWidgets.QMainWindow()
        self.evaluateScreen = Ui_EvaluateWindow()
        self.evaluateScreen.setupUi(self.evaluateDialog)

    def setupUi(self, MainWindow):

        self._batsman_count = 0
        self._bowlers_count = 0
        self._allrounders_count = 0
        self._wicketkeeper_count = 0
        self._total_count = 0

        self.points_available = 1000
        self.points_used = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 590)
        self.MainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Points_available_label = QtWidgets.QLabel(self.centralwidget)
        self.Points_available_label.setGeometry(QtCore.QRect(50, 130, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Points_available_label.setFont(font)
        self.Points_available_label.setObjectName("Points_available_label")
        
        self.Points_use_label = QtWidgets.QLabel(self.centralwidget)
        self.Points_use_label.setGeometry(QtCore.QRect(420, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Points_use_label.setFont(font)
        self.Points_use_label.setObjectName("Points_use_label")
        
        self.Players_Available_list = QtWidgets.QListWidget(self.centralwidget)
        self.Players_Available_list.setGeometry(QtCore.QRect(50, 160, 271, 351))
        self.Players_Available_list.setObjectName("Players_Available_list")

        self.Players_Selected_list = QtWidgets.QListWidget(self.centralwidget)
        self.Players_Selected_list.setGeometry(QtCore.QRect(420, 160, 271, 351))
        self.Players_Selected_list.setObjectName("Players_Selected_list")

        # For Spacing adjustment
        self.tempListItem(self.Players_Selected_list)
        self.tempListItem(self.Players_Selected_list)

        self.Batsman_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Batsman_radio.setGeometry(QtCore.QRect(60, 170, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Batsman_radio.setFont(font)
        self.Batsman_radio.setObjectName("Batsman_radio")
        
        self.Bowlers_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Bowlers_radio.setGeometry(QtCore.QRect(120, 170, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Bowlers_radio.setFont(font)
        self.Bowlers_radio.setObjectName("Bowlers_radio")
        
        self.Allrounders_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Allrounders_radio.setGeometry(QtCore.QRect(180, 170, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Allrounders_radio.setFont(font)
        self.Allrounders_radio.setObjectName("Allrounders_radio")
        
        self.Wicketkeeper_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Wicketkeeper_radio.setGeometry(QtCore.QRect(230, 170, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Wicketkeeper_radio.setFont(font)
        self.Wicketkeeper_radio.setObjectName("Wicketkeeper_radio")
        
        self.Points_available_count = QtWidgets.QLabel(self.centralwidget)
        self.Points_available_count.setGeometry(QtCore.QRect(170, 130, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Points_available_count.setFont(font)
        self.Points_available_count.setObjectName("Points_available_count")
        
        self.Points_use_count = QtWidgets.QLabel(self.centralwidget)
        self.Points_use_count.setGeometry(QtCore.QRect(510, 130, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Points_use_count.setFont(font)
        self.Points_use_count.setObjectName("Points_use_count")
        
        self.Selection_tag = QtWidgets.QLabel(self.centralwidget)
        self.Selection_tag.setGeometry(QtCore.QRect(40, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Selection_tag.setFont(font)
        self.Selection_tag.setObjectName("Selection_tag")
        
        self.Batsman_label = QtWidgets.QLabel(self.centralwidget)
        self.Batsman_label.setGeometry(QtCore.QRect(20, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Batsman_label.setFont(font)
        self.Batsman_label.setObjectName("Batsman_label")
        
        self.Batsman_count = QtWidgets.QLabel(self.centralwidget)
        self.Batsman_count.setGeometry(QtCore.QRect(130, 60, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Batsman_count.setFont(font)
        self.Batsman_count.setObjectName("Batsman_count")
        
        self.Bowlers_label = QtWidgets.QLabel(self.centralwidget)
        self.Bowlers_label.setGeometry(QtCore.QRect(190, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bowlers_label.setFont(font)
        self.Bowlers_label.setObjectName("Bowlers_label")

        self.Bowlers_count = QtWidgets.QLabel(self.centralwidget)
        self.Bowlers_count.setGeometry(QtCore.QRect(300, 60, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bowlers_count.setFont(font)
        self.Bowlers_count.setObjectName("Bowlers_count")
        
        self.Allrounders_label = QtWidgets.QLabel(self.centralwidget)
        self.Allrounders_label.setGeometry(QtCore.QRect(360, 60, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Allrounders_label.setFont(font)
        self.Allrounders_label.setObjectName("Allrounders_label")

        self.Wicketkeeper_label = QtWidgets.QLabel(self.centralwidget)
        self.Wicketkeeper_label.setGeometry(QtCore.QRect(540, 60, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Wicketkeeper_label.setFont(font)
        self.Wicketkeeper_label.setObjectName("Wicketkeeper_label")

        self.Allrounders_count = QtWidgets.QLabel(self.centralwidget)
        self.Allrounders_count.setGeometry(QtCore.QRect(480, 60, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Allrounders_count.setFont(font)
        self.Allrounders_count.setObjectName("Allrounders_count")

        self.Wicketkeeper_count = QtWidgets.QLabel(self.centralwidget)
        self.Wicketkeeper_count.setGeometry(QtCore.QRect(690, 60, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Wicketkeeper_count.setFont(font)
        self.Wicketkeeper_count.setObjectName("Wicketkeeper_count")

        self.Team_name_label = QtWidgets.QLabel(self.centralwidget)
        self.Team_name_label.setGeometry(QtCore.QRect(440, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Team_name_label.setFont(font)
        self.Team_name_label.setObjectName("Team_name_label")

        self.Team_name_displayer = QtWidgets.QLabel(self.centralwidget)
        self.Team_name_displayer.setGeometry(QtCore.QRect(550, 170, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Team_name_displayer.setFont(font)
        self.Team_name_displayer.setObjectName("Team_name_displayer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 21))
        self.menubar.setObjectName("menubar")

        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.actionNEW_Team.triggered.connect(self.newFile)

        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.actionOPEN_Team.triggered.connect(self.openFile)
        
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.actionSAVE_Team.triggered.connect(self.saveFile)
        
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.actionEVALUATE_Team.triggered.connect(self.evaluateFile)

        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Choice Selector
        self.Batsman_radio.clicked.connect(self.load_names)
        self.Bowlers_radio.clicked.connect(self.load_names)
        self.Allrounders_radio.clicked.connect(self.load_names)
        self.Wicketkeeper_radio.clicked.connect(self.load_names)

        # Player Adding
        self.Players_Available_list.itemDoubleClicked.connect(self.removeList1)
        self.Players_Selected_list.itemDoubleClicked.connect(self.removeList2)

        self.items = []

        self.newScreen.pushButton.clicked.connect(self.nameDisplay)
        self.openScreen.openButton.clicked.connect(self.openClicked)
        self.evaluateScreen.TeamName_dropdown.currentTextChanged.connect(self.TeamName_dropdown_changer)
        self.evaluateScreen.Calculate_button.clicked.connect(self.evaluateScore)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.Points_available_label.setText(_translate("MainWindow", "Points Available"))
        self.Points_use_label.setText(_translate("MainWindow", "Points Used"))
        self.Batsman_radio.setText(_translate("MainWindow", "BAT"))
        self.Bowlers_radio.setText(_translate("MainWindow", "BOW"))
        self.Allrounders_radio.setText(_translate("MainWindow", "AR"))
        self.Wicketkeeper_radio.setText(_translate("MainWindow", "WK"))
        self.Points_available_count.setText(_translate("MainWindow", "####"))
        self.Points_use_count.setText(_translate("MainWindow", "####"))
        self.Selection_tag.setText(_translate("MainWindow", "Yours Selections"))
        self.Batsman_label.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.Batsman_count.setText(_translate("MainWindow", "##"))
        self.Bowlers_label.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.Bowlers_count.setText(_translate("MainWindow", "##"))
        self.Allrounders_label.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.Wicketkeeper_label.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.Allrounders_count.setText(_translate("MainWindow", "##"))
        self.Wicketkeeper_count.setText(_translate("MainWindow", "##"))
        self.Team_name_label.setText(_translate("MainWindow", "Team Name"))
        self.Team_name_displayer.setText(_translate("MainWindow", "####"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def tempListItem(self, where):
        temp = QtWidgets.QListWidgetItem("")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        temp.setFont(font)
        where.addItem(temp)

    def newFile(self):
        self.newDialog.show()
    
    def openFile(self):
        self.openDialog.show()

    def saveFile(self):
        for index in range(self.Players_Selected_list.count()):
            self.items.append(str(self.Players_Selected_list.item(index).text()))
        Team = sqlite3.connect('TEAM.db')
        cursor = Team.cursor()
        teamName = self.Team_name_displayer.text()
        self.items = self.items[2:]
        for player in self.items:
            cursor.execute("INSERT INTO teams ('player', 'team_name') VALUES ('%s', '%s')" % (player, teamName))
        self.items = []
        Team.commit()
        Team.close()

    def evaluateFile(self):
        self.evaluateDialog.show()

    def TeamName_dropdown_changer(self):
        self.evaluateScreen.Players_list.clear()
        self.evaluateScreen.Points_list.clear()
        self.evaluateScreen.Points.clear()
        self.evaluateScreen.MatchName_dropdown.currentTextChanged.connect(self.MatchName_dropdown_changer)

    def MatchName_dropdown_changer(self):
        self.evaluateScreen.Players_list.clear()
        self.evaluateScreen.Points_list.clear()
        Team = sqlite3.connect("TEAM.db")
        cursor = Team.cursor()
        teamName = self.evaluateScreen.TeamName_dropdown.currentText()
        cursor.execute("SELECT player FROM teams WHERE team_name = '" + teamName + "';")
        players = cursor.fetchall()
        players = [a[0] for a in players]

        for player in players:
            item = QtWidgets.QListWidgetItem(player)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.evaluateScreen.Players_list.addItem(item)

        self.scores = []

        Match = sqlite3.connect("MATCH.db")
        cursor3 = Match.cursor()

        for player in players:
            cursor3.execute("SELECT points FROM match WHERE match_no = '1' AND player = '" + player + "';")
            self.scores.append(cursor3.fetchone()[0])

        for score in map(str, self.scores):
            item = QtWidgets.QListWidgetItem(score)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#fdc086'))
            self.evaluateScreen.Points_list.addItem(item)

        Match.close()
        Team.close()
        
    def evaluateScore(self):
        self.evaluateScreen.Points.setText(str(sum(self.scores)))

    def nameDisplay(self):
        teamName = self.newScreen.name_box.text()
        self.Players_Selected_list.clear()
        self.Players_Available_list.clear()

        # Space adjustment
        self.tempListItem(self.Players_Selected_list)
        self.tempListItem(self.Players_Selected_list)

        self.Team_name_displayer.setText(teamName)
        self.Points_available_count.setText(str(self.points_available))
        self.Points_use_count.setText(str(self.points_used))
        self.newDialog.close()

    def openClicked(self):
        self.Players_Selected_list.clear()
        self.tempListItem(self.Players_Selected_list)
        self.tempListItem(self.Players_Selected_list)
        values = 0

        try:
            teamName = self.openScreen.openName_box.text()
            self.Team_name_displayer.setText(teamName)
            Team = sqlite3.connect('TEAM.db')
            cursor = Team.cursor()
            Players = sqlite3.connect("PLAYERS.db")
            cursor2 = Players.cursor()
            cursor.execute("SELECT player FROM teams WHERE team_name = '" + teamName + "';")
            players = cursor.fetchall()
            players = [a[0] for a in players]

            for player in players:
                cursor2.execute("SELECT value FROM players WHERE player = '" + player + "';")
                values += cursor2.fetchone()[0]

            for player in players:
                item = QtWidgets.QListWidgetItem(player)
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                item.setBackground(QtGui.QColor('#ffff99'))
                item.setFont(font)
                self.Players_Selected_list.addItem(item)

            self.Points_use_count.setText(str(values))
            self.Points_available_count.setText(str(1000 - values))
            values = 0
            self.openDialog.close()
            Team.close()
            Players.close()
        except Exception:
            errorDialog = QtWidgets.QErrorMessage()
            errorDialog.showMessage("File Not Found.")
            errorDialog.exec_()

    def load_names(self):
        Batsman = 'BAT'
        Bowlers = 'BWL'
        WicketKeeper = 'WK'
        Allrounder = 'AR'

        Players = sqlite3.connect("PLAYERS.db")
        cursor2 = Players.cursor()

        l1 = "SELECT player FROM players WHERE ctg = '" + Batsman + "';"
        l2 = "SELECT player FROM players WHERE ctg = '" + Bowlers + "';"
        l3 = "SELECT player FROM players WHERE ctg = '" + WicketKeeper + "';"
        l4 = "SELECT player FROM players WHERE ctg = '" + Allrounder + "';"

        if self.Batsman_radio.isChecked() == True:
            cursor2.execute(l1)
            BT = cursor2.fetchall()
            self.Players_Available_list.clear()
            self.tempListItem(self.Players_Available_list)
            self.tempListItem(self.Players_Available_list)
            for i in range(len(BT)):
                item1 = QtWidgets.QListWidgetItem(BT[i][0])
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                item1.setFont(font)
                self.Players_Available_list.addItem(item1)

        if self.Bowlers_radio.isChecked() == True:
            cursor2.execute(l2)
            BL = cursor2.fetchall()
            self.Players_Available_list.clear()
            self.tempListItem(self.Players_Available_list)
            self.tempListItem(self.Players_Available_list)
            for i in range(len(BL)):
                item2 = QtWidgets.QListWidgetItem(BL[i][0])
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setBold(True)
                font.setWeight(75)
                font.setPointSize(10)
                item2.setFont(font)
                self.Players_Available_list.addItem(item2)

        if self.Wicketkeeper_radio.isChecked() == True:
            cursor2.execute(l3)
            WK = cursor2.fetchall()
            self.Players_Available_list.clear()
            self.tempListItem(self.Players_Available_list)
            self.tempListItem(self.Players_Available_list)
            for i in range(len(WK)):
                item3 = QtWidgets.QListWidgetItem(WK[i][0])
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setBold(True)
                font.setWeight(75)
                font.setPointSize(10)
                item3.setFont(font)
                self.Players_Available_list.addItem(item3)

        if self.Allrounders_radio.isChecked() == True:
            cursor2.execute(l4)
            AR = cursor2.fetchall()
            self.Players_Available_list.clear()
            self.tempListItem(self.Players_Available_list)
            self.tempListItem(self.Players_Available_list)
            for i in range(len(AR)):
                item4 = QtWidgets.QListWidgetItem(AR[i][0])
                font = QtGui.QFont()
                font.setFamily("Comic Sans MS")
                font.setBold(True)
                font.setWeight(75)
                font.setPointSize(10)
                item4.setFont(font)
                self.Players_Available_list.addItem(item4)

        Players.close()

    def getValue(self, name):
        Players = sqlite3.connect("PLAYERS.db")
        cursor2 = Players.cursor()
        cursor2.execute("SELECT value FROM players WHERE player = '" + name + "';")
        value = cursor2.fetchone()[0]
        Players.close()
        return value

    def removeList1(self, item):
        if self.Batsman_radio.isChecked() == True:
            name = self.Players_Available_list.currentItem().text()
            self.Players_Available_list.takeItem(self.Players_Available_list.row(item))
            value = self.getValue(name)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(10)
            item.setFont(font)
            self.Players_Selected_list.addItem(item)
            self._batsman_count += 1
            self._total_count = self.Players_Selected_list.count()
            self.error()
            self.points_used += value
            self.points_available -= value
            self.Points_use_count.setText(str(self.points_used))
            self.Points_available_count.setText(str(self.points_available))
            self.Batsman_count.setText(str(self._batsman_count))
        
        elif self.Bowlers_radio.isChecked() == True:
            name = self.Players_Available_list.currentItem().text()
            self.Players_Available_list.takeItem(self.Players_Available_list.row(item))
            value = self.getValue(name)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(10)
            item.setFont(font)
            self.Players_Selected_list.addItem(item)
            self._bowlers_count += 1
            self._total_count = self.Players_Selected_list.count()
            self.error()
            self.points_used += value
            self.points_available -= value
            self.Points_use_count.setText(str(self.points_used))
            self.Points_available_count.setText(str(self.points_available))
            self.Bowlers_count.setText(str(self._bowlers_count))
        
        elif self.Wicketkeeper_radio.isChecked() == True:
            name = self.Players_Available_list.currentItem().text()
            self.Players_Available_list.takeItem(self.Players_Available_list.row(item))
            value = self.getValue(name)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(10)
            item.setFont(font)
            self.Players_Selected_list.addItem(item)
            self._wicketkeeper_count += 1
            self._total_count = self.Players_Selected_list.count()
            self.error()
            self.points_used += value
            self.points_available -= value
            self.Points_use_count.setText(str(self.points_used))
            self.Points_available_count.setText(str(self.points_available))
            self.Wicketkeeper_count.setText(str(self._wicketkeeper_count))
        
        elif self.Allrounders_radio.isChecked() == True:
            name = self.Players_Available_list.currentItem().text()
            self.Players_Available_list.takeItem(self.Players_Available_list.row(item))
            value = self.getValue(name)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(10)
            item.setFont(font)
            self.Players_Selected_list.addItem(item)
            self._allrounders_count += 1
            self._total_count = self.Players_Selected_list.count()
            self.error()
            self.points_used += value
            self.points_available -= value
            self.Points_use_count.setText(str(self.points_used))
            self.Points_available_count.setText(str(self.points_available))
            self.Allrounders_count.setText(str(self._allrounders_count))

    def removeList2(self, item):
        if self.Batsman_radio.isChecked() == True:
            name = self.Players_Selected_list.currentItem().text()
            self.Players_Selected_list.takeItem(self.Players_Selected_list.row(item))
            value = self.getValue(name)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(10)
            item.setFont(font)
            self.Players_Available_list.addItem(item)
            self._batsman_count -= 1
            self._total_count = self.Players_Selected_list.count()
            self.error()
            self.points_used -= value
            self.points_available += value
            self.Points_use_count.setText(str(self.points_used))
            self.Points_available_count.setText(str(self.points_available))
            self.Batsman_count.setText(str(self._batsman_count))
        
        elif self.Bowlers_radio.isChecked() == True:
            name = self.Players_Selected_list.currentItem().text()
            self.Players_Selected_list.takeItem(self.Players_Selected_list.row(item))
            value = self.getValue(name)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(10)
            item.setFont(font)
            self.Players_Available_list.addItem(item)
            self._bowlers_count -= 1
            self._total_count = self.Players_Selected_list.count()
            self.error()
            self.points_used -= value
            self.points_available += value
            self.Points_use_count.setText(str(self.points_used))
            self.Points_available_count.setText(str(self.points_available))
            self.Bowlers_count.setText(str(self._bowlers_count))
        
        elif self.Wicketkeeper_radio.isChecked() == True:
            name = self.Players_Selected_list.currentItem().text()
            self.Players_Selected_list.takeItem(self.Players_Selected_list.row(item))
            value = self.getValue(name)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(10)
            item.setFont(font)
            self.Players_Available_list.addItem(item)
            self._wicketkeeper_count -= 1
            self._total_count = self.Players_Selected_list.count()
            self.error()
            self.points_used -= value
            self.points_available += value
            self.Points_use_count.setText(str(self.points_used))
            self.Points_available_count.setText(str(self.points_available))
            self.Wicketkeeper_count.setText(str(self._wicketkeeper_count))
        
        elif self.Allrounders_radio.isChecked() == True:
            name = self.Players_Selected_list.currentItem().text()
            self.Players_Selected_list.takeItem(self.Players_Selected_list.row(item))
            value = self.getValue(name)
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setBold(True)
            font.setWeight(75)
            font.setPointSize(10)
            item.setFont(font)
            self.Players_Available_list.addItem(item)
            self._allrounders_count -= 1
            self._total_count = self.Players_Selected_list.count()
            self.error()
            self.points_used -= value
            self.points_available += value
            self.Points_use_count.setText(str(self.points_used))
            self.Points_available_count.setText(str(self.points_available))
            self.Allrounders_count.setText(str(self._allrounders_count))

    def error(self):
        errorDialog = QtWidgets.QErrorMessage()

        if self._batsman_count >= 0 and self._batsman_count < 6:
            pass
        else:
            errorDialog.showMessage("Oh no! Only 5 batsman are allowed.")
            errorDialog.exec_()
        
        if self._bowlers_count >= 0 and self._bowlers_count < 6:
            pass
        else:
            errorDialog.showMessage("Oh no! Only 5 bowlers are allowed.")
            errorDialog.exec_()
        
        if self._wicketkeeper_count >=0 and self._wicketkeeper_count < 2:
            pass
        else:
            errorDialog.showMessage("Oh no! Only 1 keeper are allowed.")
            errorDialog.exec_()
        
        if self._allrounders_count >= 0 and self._allrounders_count < 3:
            pass
        else:
            errorDialog.showMessage("Oh no! Only 2 All-rounders are allowed")
            errorDialog.exec_()

        if self._total_count >= 0 and self._total_count < 14:
            pass
        else:
            errorDialog.showMessage("Oh no! No more than 11 Players are allowed.")
            errorDialog.exec_()

        if self.points_used > 1000:
            errorDialog.showMessage("Oh no! Only 1000 points can be used.")
            errorDialog.exec_()


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(App.exec_())
