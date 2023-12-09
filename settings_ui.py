from PyQt5 import QtCore, QtWidgets
from config import settings_background, widget_style_template, hover_style_template

background_color = "rgb(136, 173, 102)"
exit_background_color = "rgb(40, 80, 89)"
exit_hover_color = "rgb(55, 89, 44)"


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(800, 600)

        Settings.setStyleSheet("QMainWindow{background-image: url(" +
                               str(settings_background).replace("\\", "/") + "); background-position: center;}")

        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-image: none;")

        self.heaps_label = QtWidgets.QLabel(self.centralwidget)
        self.heaps_label.setGeometry(QtCore.QRect(125, 50, 500, 100))
        self.heaps_label.setObjectName("heaps_label")
        self.heaps_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.heaps_label.setStyleSheet(
            widget_style_template.format(widget_type="QLabel", font_size=20, border_color="black",
                                         background_color=background_color,
                                         text_color="black")[:-1] + ";padding-left: 50px;}")


        self.solo_label = QtWidgets.QLabel(self.centralwidget)
        self.solo_label.setGeometry(QtCore.QRect(125, 180, 500, 70))
        self.solo_label.setObjectName("solo_label")
        self.solo_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.solo_label.setStyleSheet(
            widget_style_template.format(widget_type="QLabel", font_size=20, border_color="black",
                                         background_color=background_color,
                                         text_color="black")[:-1] + ";padding-left: 50px;}")


        self.turn_label = QtWidgets.QLabel(self.centralwidget)
        self.turn_label.setGeometry(QtCore.QRect(125, 310, 500, 70))
        self.turn_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.turn_label.setObjectName("turn_label")
        self.turn_label.setStyleSheet(
            widget_style_template.format(widget_type="QLabel", font_size=20, border_color="black",
                                         background_color=background_color,
                                         text_color="black")[:-1] + ";padding-left: 50px;}")


        self.solo_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.solo_checkBox.setGeometry(QtCore.QRect(400, 200, 250, 25))
        self.solo_checkBox.setStyleSheet("")
        self.solo_checkBox.setIconSize(QtCore.QSize(25, 25))
        self.solo_checkBox.setObjectName("solo_checkBox")

        self.turn_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.turn_checkBox.setGeometry(QtCore.QRect(400, 330, 250, 25))
        self.turn_checkBox.setIconSize(QtCore.QSize(25, 25))
        self.turn_checkBox.setObjectName("turn_checkBox")

        self.heaps_input = QtWidgets.QLineEdit(self.centralwidget)
        self.heaps_input.setGeometry(QtCore.QRect(400, 65, 205, 70))
        self.heaps_input.setObjectName("heaps_input")
        self.heaps_input.setStyleSheet(
            widget_style_template.format(widget_type="QLineEdit", font_size=10, border_color="black",
                                         background_color=background_color,
                                         text_color="black")[:-1] + ";padding-left: 5px;}")


        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(450, 490, 250, 70))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.setStyleSheet(
            widget_style_template.format(widget_type="QPushButton", font_size=20, border_color="black",
                                         background_color=exit_background_color,
                                         text_color="black") +
            hover_style_template.format(widget_type="QPushButton", hover_color=exit_hover_color))


        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(100, 490, 250, 70))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setStyleSheet(
            widget_style_template.format(widget_type="QPushButton", font_size=20, border_color="black",
                                         background_color=exit_background_color,
                                         text_color="black") +
            hover_style_template.format(widget_type="QPushButton", hover_color=exit_hover_color))


        self.saved_label = QtWidgets.QLabel(self.centralwidget)
        self.saved_label.setGeometry(QtCore.QRect(100, 460, 250, 20))
        self.saved_label.setText("")
        self.saved_label.setAlignment(QtCore.Qt.AlignCenter)
        self.saved_label.setObjectName("saved_label")
        self.saved_label.setStyleSheet(
            widget_style_template.format(widget_type="QLabel", font_size=10, border_color="black",
                                         background_color=background_color,
                                         text_color="black")[:-1] + ";margin: 80px 80px;}")

        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "MainWindow"))
        self.heaps_label.setText(_translate("Settings",
                                            "<html><head/><body><p><span style=\" font-size:18pt;\">Enter heaps count <br/>(Ex. [3, 4, 5]) <br/>(heaps max=6) </span></p></body></html>"))
        self.solo_label.setText(_translate("Settings",
                                           "<html><head/><body><p><span style=\" font-size:18pt;\">Solo mode?</span></p></body></html>"))
        self.turn_label.setText(_translate("Settings",
                                           "<html><head/><body><p><span style=\" font-size:18pt;\">Player first turn?</span></p></body></html>"))
        self.exit_btn.setText(_translate("Settings", "Exit"))
        self.save_btn.setText(_translate("Settings", "Save Settings"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QMainWindow()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
