# Form implementation generated from reading ui file 'medium_level_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        MainWindow1.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 130, 341, 361))
        self.label_2.setStyleSheet("background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 24px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 60, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 12px;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton1_medium = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton1_medium.setGeometry(QtCore.QRect(270, 170, 51, 51))
        self.pushButton1_medium.setObjectName("pushButton1_medium")
        self.pushButton2_medium = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton2_medium.setGeometry(QtCore.QRect(330, 170, 51, 51))
        self.pushButton2_medium.setObjectName("pushButton2_medium")
        self.pushButton3_medium = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton3_medium.setGeometry(QtCore.QRect(390, 170, 51, 51))
        self.pushButton3_medium.setObjectName("pushButton3_medium")
        self.pushButton4_medium = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton4_medium.setGeometry(QtCore.QRect(450, 170, 51, 51))
        self.pushButton4_medium.setObjectName("pushButton4_medium")
        self.pushButton5_medium = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton5_medium.setGeometry(QtCore.QRect(510, 170, 51, 51))
        self.pushButton5_medium.setObjectName("pushButton5_medium")
        self.pushButton_medium_level_27 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_medium_level_27.setGeometry(QtCore.QRect(20, 540, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_medium_level_27.setFont(font)
        self.pushButton_medium_level_27.setStyleSheet("QPushButton {\n"
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
"}")
        self.pushButton_medium_level_27.setObjectName("pushButton_medium_level_27")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 12px;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        MainWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Переливание"))
        self.label_3.setText(_translate("MainWindow1", "Выберите уровень"))
        self.pushButton1_medium.setText(_translate("MainWindow1", "1"))
        self.pushButton2_medium.setText(_translate("MainWindow1", "2"))
        self.pushButton3_medium.setText(_translate("MainWindow1", "3"))
        self.pushButton4_medium.setText(_translate("MainWindow1", "4"))
        self.pushButton5_medium.setText(_translate("MainWindow1", "5"))
        self.pushButton_medium_level_27.setText(_translate("MainWindow1", "Меню"))
        self.label.setText(_translate("MainWindow1", "Средний"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec())
