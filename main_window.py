# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 592)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,205,70);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,245,80);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 330, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,205,70);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,245,80);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, -5, 811, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/b94371ba97483cbfa1643d7905f3b01b.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Переливание"))
        self.pushButton.setText(_translate("MainWindow", "Играть"))
        self.pushButton_2.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
