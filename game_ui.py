from PyQt5 import QtCore, QtWidgets
from config import game_background, widget_style_template, hover_style_template


background_color = "rgb(136, 173, 102)"
hover_color = "rgb(209, 133, 46)"


class Ui_GameUi(object):
    def setupUi(self, GameUi):
        GameUi.setObjectName("GameUi")

        GameUi.setStyleSheet("QMainWindow{background-image: url(" +
                                 str(game_background).replace("\\", "/") + "); background-position: center;}")
        self.centralwidget = QtWidgets.QWidget(GameUi)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget.setStyleSheet("background-image: none;")

        self.skip_turn = QtWidgets.QPushButton(self.centralwidget)
        self.skip_turn.setGeometry(QtCore.QRect(240, 520, 320, 100))
        self.skip_turn.setObjectName("skip_turn")
        self.skip_turn.setStyleSheet(
            widget_style_template.format(widget_type="QPushButton", font_size=20, border_color="black",
                                         background_color=background_color,
                                         text_color="black") +
            hover_style_template.format(widget_type="QPushButton", hover_color=hover_color))

        self.turn_label = QtWidgets.QLabel(self.centralwidget)
        self.turn_label.setGeometry(QtCore.QRect(240, 10, 320, 100))
        self.turn_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.turn_label.setObjectName("turn_label")
        self.turn_label.setStyleSheet("""
            QLabel {
                font: 20pt "MS Shell Dlg 2";
            }
        """)

        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 30, 40, 50))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.setStyleSheet("""
            QPushButton {
                font: 20pt "MS Shell Dlg 2";
                border: none;
            }
            QPushButton:hover {
                border-radius: 1px;
                border: 1px solid red;
            }
        """)

        self.setting_btn = QtWidgets.QPushButton(self.centralwidget)
        self.setting_btn.setGeometry(QtCore.QRect(80, 30, 50, 50))
        self.setting_btn.setObjectName("setting_btn")
        self.setting_btn.setStyleSheet("""
            QPushButton {
                font: 20pt "MS Shell Dlg 2";
                border: none;

            }
            QPushButton:hover {
                border-radius: 1px;
                border: 1px solid red;
            }
        """)

        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(610, 520, 90, 100))
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.setStyleSheet(
            widget_style_template.format(widget_type="QPushButton", font_size=20, border_color="black",
                                         background_color=background_color,
                                         text_color="black") +
            hover_style_template.format(widget_type="QPushButton", hover_color=hover_color))

        GameUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameUi)
        QtCore.QMetaObject.connectSlotsByName(GameUi)

    def retranslateUi(self, GameUi):
        _translate = QtCore.QCoreApplication.translate
        GameUi.setWindowTitle(_translate("GameUi", "MainWindow"))
        self.skip_turn.setText(_translate("GameUi", "Skip turn"))
        self.turn_label.setText(_translate("GameUi", "NimGame"))

        self.back_btn.setText(_translate("GameUi", "←"))
        self.setting_btn.setText(_translate("GameUi", "⚙"))
        self.reset_btn.setText(_translate("GameUi", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameUi = QtWidgets.QMainWindow()
    ui = Ui_GameUi()
    ui.setupUi(GameUi)
    GameUi.show()
    sys.exit(app.exec_())
