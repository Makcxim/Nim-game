from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QMovie
from config import main_background, main_gif, hover_style_template

background_color = "rgb(136, 173, 102)"
hover_color = "rgb(209, 133, 46)"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("NimGame")
        MainWindow.setObjectName("NimGame")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)

        MainWindow.setStyleSheet("QMainWindow{background-image: url(" +
                                 str(main_background).replace("\\", "/") + "); background-position: center;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget.setStyleSheet("background-image: none;")
        self.game_label = QtWidgets.QLabel(self.centralwidget)
        self.game_label.setGeometry(QtCore.QRect(0, 50, 800, 100))
        self.game_label.setStyleSheet("font: 50pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255);")
        self.game_label.setScaledContents(False)
        self.game_label.setAlignment(QtCore.Qt.AlignCenter)
        self.game_label.setObjectName("game_label")

        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(240, 180, 320, 100))
        self.play_btn.setObjectName("play_btn")
        self.play_btn.setStyleSheet("""
        QPushButton {
            font: 30pt "MS Shell Dlg 2";
            border-radius: 50px;
            border: 2px solid black;
            background-color: rgb(136, 173, 102);
        }""" +
                                    hover_style_template.format(widget_type="QPushButton", hover_color=hover_color))

        self.settings_btn = QtWidgets.QPushButton(self.centralwidget)
        self.settings_btn.setGeometry(QtCore.QRect(240, 300, 320, 100))
        self.settings_btn.setObjectName("settings_btn")
        self.settings_btn.setStyleSheet("""
        QPushButton {
            font: 30pt "MS Shell Dlg 2";
            border-radius: 50px;
            border: 2px solid black;
            background-color: rgb(136, 173, 102);
        }""" +
                                        hover_style_template.format(widget_type="QPushButton", hover_color=hover_color))

        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(240, 420, 320, 100))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.setStyleSheet("""
        QPushButton {
            font: 30pt "MS Shell Dlg 2";
            border-radius: 50px;
            border: 2px solid black;
            background-color: rgb(136, 173, 102);
        }""" +
                                    hover_style_template.format(widget_type="QPushButton", hover_color=hover_color))

        self.amogus_label = QtWidgets.QLabel(self.centralwidget)
        self.amogus_label.setGeometry(QtCore.QRect(20, 230, 200, 240))
        self.exit_btn.setObjectName("amogus_label")
        self.amogus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.movie = QMovie(str(main_gif))
        self.amogus_label.setMovie(self.movie)
        self.movie.start()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NimGame"))
        self.game_label.setText(_translate("MainWindow", "Best NimGame "))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.settings_btn.setText(_translate("MainWindow", "Settings"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
