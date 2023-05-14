# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Task import *
from DBHandler import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 591)
        MainWindow.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 191, 611))
        self.frame.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addTaskMenu = QtWidgets.QPushButton(self.frame)
        self.addTaskMenu.setGeometry(QtCore.QRect(10, 30, 171, 51))
        self.addTaskMenu.clicked.connect(self.showAddTaskFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addTaskMenu.setFont(font)
        self.addTaskMenu.setStyleSheet("background-color: rgb(255, 0, 127);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new task.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTaskMenu.setIcon(icon)
        self.addTaskMenu.setIconSize(QtCore.QSize(40, 40))
        self.addTaskMenu.setObjectName("addTaskMenu")
        self.listTaskMenu = QtWidgets.QPushButton(self.frame)
        self.listTaskMenu.setGeometry(QtCore.QRect(10, 250, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.listTaskMenu.setFont(font)
        self.listTaskMenu.setStyleSheet("background-color: rgb(255, 0, 127);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/view task.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listTaskMenu.setIcon(icon1)
        self.listTaskMenu.setIconSize(QtCore.QSize(40, 40))
        self.listTaskMenu.setObjectName("listTaskMenu")
        self.listTaskMenu.clicked.connect(self.showListTaskFrame)
        self.searchTaskMenu = QtWidgets.QPushButton(self.frame)
        self.searchTaskMenu.setGeometry(QtCore.QRect(10, 470, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.searchTaskMenu.setFont(font)
        self.searchTaskMenu.setStyleSheet("background-color: rgb(255, 0, 127);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/search icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchTaskMenu.setIcon(icon2)
        self.searchTaskMenu.setIconSize(QtCore.QSize(40, 40))
        self.searchTaskMenu.setObjectName("searchTaskMenu")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(190, 10, 601, 571))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.calendarAddTask = QtWidgets.QCalendarWidget(self.frame_2)
        self.calendarAddTask.setGeometry(QtCore.QRect(160, 20, 311, 171))
        self.calendarAddTask.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.calendarAddTask.setObjectName("calendarAddTask")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 255);")
        self.label.setObjectName("label")
        self.addTaskTime = QtWidgets.QTimeEdit(self.frame_2)
        self.addTaskTime.setGeometry(QtCore.QRect(160, 210, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addTaskTime.setFont(font)
        self.addTaskTime.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.addTaskTime.setObjectName("addTaskTime")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.taskNameEdit = QtWidgets.QLineEdit(self.frame_2)
        self.taskNameEdit.setGeometry(QtCore.QRect(160, 270, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.taskNameEdit.setFont(font)
        self.taskNameEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.taskNameEdit.setObjectName("taskNameEdit")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_3.setObjectName("label_3")
        self.tasDescEdit = QtWidgets.QPlainTextEdit(self.frame_2)
        self.tasDescEdit.setGeometry(QtCore.QRect(160, 330, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tasDescEdit.setFont(font)
        self.tasDescEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tasDescEdit.setObjectName("tasDescEdit")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(420, 480, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(190, 10, 601, 571))
        self.frame_3.setStyleSheet("color: rgb(85, 170, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.todayTaskTable = QtWidgets.QTableView(self.frame_3)
        self.todayTaskTable.setGeometry(QtCore.QRect(130, 70, 361, 201))
        self.todayTaskTable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.todayTaskTable.setDragDropOverwriteMode(False)
        self.todayTaskTable.setObjectName("todayTaskTable")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.todaysTaskTitle = QtWidgets.QLineEdit(self.frame_3)
        self.todaysTaskTitle.setGeometry(QtCore.QRect(130, 300, 361, 31))
        self.todaysTaskTitle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.todaysTaskTitle.setObjectName("todaysTaskTitle")
        self.todaysTaskDesc = QtWidgets.QPlainTextEdit(self.frame_3)
        self.todaysTaskDesc.setGeometry(QtCore.QRect(130, 360, 361, 101))
        self.todaysTaskDesc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.todaysTaskDesc.setObjectName("todaysTaskDesc")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 480, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(85, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addTaskMenu.setText(_translate("MainWindow", "Add Task"))
        self.listTaskMenu.setText(_translate("MainWindow", "List Tasks"))
        self.searchTaskMenu.setText(_translate("MainWindow", "Search Task"))
        self.label.setText(_translate("MainWindow", "Select Date"))
        self.label_2.setText(_translate("MainWindow", "Select Time"))
        self.label_3.setText(_translate("MainWindow", "Task Title"))
        self.label_4.setText(_translate("MainWindow", "Description"))
        self.pushButton.setText(_translate("MainWindow", "Add Task"))
        self.label_5.setText(_translate("MainWindow", "Today\'s Tasks"))
        self.pushButton_2.setText(_translate("MainWindow", "View Task"))

        self.pushButton.clicked.connect(self.addTaskBtnClicked)
        self.pushButton_2.clicked.connect(self.showDetails)

    def showAddTaskFrame(self):
        self.frame_2.show()
        self.frame_3.hide()

    def showListTaskFrame(self):
        self.frame_2.hide()
        self.frame_3.show()
        date = self.calendarAddTask.selectedDate().toString()
        db = DBHandler()
        rows = db.getTasks(date)

        self.todayTaskTable.setSelectionBehavior(1)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["ID", "Title", "Description", "Date", "Time"])
        try:
            i = 0
            for row in rows:
                for column in range(0, 5):
                    item = QStandardItem(str(row[column]))
                    model.setItem(i, column, item)
                i = i + 1
            self.todayTaskTable.setModel(model)
        except Exception as e:
            print(e)

    def addTaskBtnClicked(self):
        taskDate = self.calendarAddTask.selectedDate().toString()
        taskTime = self.addTaskTime.time().toString()
        taskTitle = self.taskNameEdit.text()
        taskDesc = self.tasDescEdit.toPlainText()

        t = Task(taskTitle, taskDesc, taskDate, taskTime)
        db = DBHandler()
        db.insertTask(t)

    def showDetails(self):
        idx = self.todayTaskTable.selectedIndexes()
        id = idx[0]
        title = idx[1]
        desc = idx[2]

        try:
            self.todaysTaskTitle.setText(title.data())
            self.todaysTaskDesc.setPlainText(desc.data())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
