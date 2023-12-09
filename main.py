import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

from start_ui import Ui_MainWindow as StartUi
from game_ui import Ui_GameUi as GameUi
from settings_ui import Ui_Settings as SettingsUi
from game_algorithm import last_not_pressed_btn, find_best_step
from config import settings_json, nim_icon, widget_style_template, hover_style_template

background_color = "rgb(136, 173, 102)"
hover_color = "rgb(209, 133, 46)"


class NimGame(QMainWindow):
    def __init__(self):
        super(NimGame, self).__init__()
        self.ui = StartUi()
        self.ui.setupUi(self)

        self.ui.play_btn.clicked.connect(self.play_btn_clicked)
        self.ui.settings_btn.clicked.connect(self.settings_button_clicked)
        self.ui.exit_btn.clicked.connect(self.exit_btn_clicked)

    def play_btn_clicked(self):
        game_ui = GameWindow()
        widget.addWidget(game_ui)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def settings_button_clicked(self):
        settings_window = SettingsWindow()
        widget.addWidget(settings_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def exit_btn_clicked(self):
        sys.exit()


def show_message_box(title, message, ok_function=None):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    style_sheet = 'QMessageBox { font-size: 16px "MS Shell Dlg 2"; }'

    msg_box.setStyleSheet(style_sheet)
    msg_box.setGeometry(screen_width + 100, screen_height + 100, 800, 600)
    msg_box.setWindowIcon(QtGui.QIcon(str(nim_icon)))
    if ok_function:
        msg_box.buttonClicked.connect(ok_function)
    msg_box.exec_()


class GameWindow(QMainWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.button_objects = None
        self.ui = GameUi()
        self.ui.setupUi(self)

        self.ui.back_btn.clicked.connect(self.exit_to_start_clicked)
        self.ui.skip_turn.clicked.connect(self.skip_turn_clicked)
        self.ui.setting_btn.clicked.connect(self.settings_button_clicked)
        self.ui.reset_btn.clicked.connect(self.reset_btn_clicked)

        self.buttons_available = True
        self.start_pos = json.loads(open(settings_json, "r").read())["heaps_count"]
        self.current_move = []
        self.pressed_buttons = {f"{_ + 1}{i}": 0 for _, j in enumerate(self.start_pos) for i in
                                range(1, int(j) + 1)}

        self.solo_mode = True if json.loads(open(settings_json, "r").read())["solo_mode"] == "True" else False
        self.create_buttons()
        self.check_first_turn()

    def create_buttons(self):
        heaps_count = len(self.start_pos)
        first_heap = [100, 410]

        if heaps_count == 2:
            first_heap = [213, first_heap[1]]

        for i in range(heaps_count):
            for _ in range(self.start_pos[i]):
                btn_name = f"btn_{i + 1}{_ + 1}"
                self.ui.button = QtWidgets.QPushButton(self.ui.centralwidget)
                self.ui.button.setGeometry(QtCore.QRect(first_heap[0], first_heap[1], 150, 50))
                self.ui.button.setObjectName(btn_name)
                self.ui.button.setText("STONE")
                self.ui.button.setStyleSheet(
                    widget_style_template.format(widget_type="QPushButton", font_size=20, border_color="black",
                                                 background_color=background_color,
                                                 text_color="black") +
                    hover_style_template.format(widget_type="QPushButton", hover_color=hover_color))
                self.ui.button.clicked.connect(self.nim_butt_clicked)
                first_heap = [first_heap[0], first_heap[1] - 60]
            first_heap = [first_heap[0] + 225, 410]

        first_heap[0] = first_heap[0] if first_heap[0] >= 800 else 800

        widget.setGeometry(abs(screen_width * 2 + 400 - first_heap[0]) // 2 + 200, screen_height, first_heap[0], 600)
        widget.setFixedSize(first_heap[0], 600)
        self.ui.skip_turn.setGeometry(first_heap[0] // 2 - 160, 540, 320, 30)
        self.ui.reset_btn.setGeometry(first_heap[0] // 2 + 210, 540, 90, 30)
        self.ui.turn_label.setGeometry(first_heap[0] // 2 - 160, 30, 320, 30)

        self.button_objects = {i.objectName(): i for i in self.findChildren(QtWidgets.QPushButton) if
                               "btn_" in i.objectName()}

    def check_first_turn(self):
        if self.solo_mode:
            return
        if json.loads(open(settings_json, "r").read())["player_first_turn"] == "False":
            self.skip_turn_clicked(mode="PC")

    def nim_butt_clicked(self):
        if not self.buttons_available:
            return

        butt: QPushButton = self.sender()  # noqa
        allowed_btn = last_not_pressed_btn(self.connect_current_pressed_btn(), len(self.start_pos))
        allowed_btn_text = [f"btn_{i}{j}" for i, j in allowed_btn.items()]

        if butt.objectName() in allowed_btn_text and \
                butt.objectName()[4] in (self.current_move[0][0] if self.current_move else butt.objectName()[4]):
            butt.setText("NOT STONE")
            butt.setStyleSheet("""
                QPushButton {
                    font: 20pt "MS Shell Dlg 2";
                    border-radius: 10px;
                    border: 2px solid black; 
                    background-color: rgb(255, 0, 0);
                }""")
            self.current_move += [butt.objectName()[4:]]

    def exit_to_start_clicked(self):
        main_window = NimGame()
        widget.setGeometry(screen_width, screen_height, 800, 600)
        widget.addWidget(main_window)
        widget.setFixedSize(800, 600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def skip_turn_clicked(self, mode=None):
        if not self.current_move and mode != "PC":
            show_message_box("NOT THIS TIME", "NOT THIS TIME...")
            return

        [self.pressed_buttons.update({i: 1}) for i in self.current_move]
        self.current_move = []

        self.check_win(turn="player")

        self.buttons_available = False

        if not self.solo_mode:
            self.pressed_buttons = find_best_step(self.pressed_buttons, len(self.start_pos))

        for key, value in self.pressed_buttons.items():
            if value == 1:
                self.button_objects[f"btn_{key}"].setText("NOT STONE")
                self.button_objects[f"btn_{key}"].setStyleSheet("""
                    QPushButton {
                        font: 20pt "MS Shell Dlg 2";
                        border-radius: 10px;
                        border: 2px solid black; 
                        background-color: rgb(0, 255, 255);
                    }
                """)

        self.buttons_available = True

        if not self.solo_mode:
            self.check_win(turn="computer")

    def check_win(self, turn="player"):
        if sum(self.pressed_buttons.values()) == sum(self.start_pos) and turn == "player":
            show_message_box("CONGRATS!", "YOU WON! \nSTARTING NEW GAME...", self.restart_game)
        elif sum(self.pressed_buttons.values()) == sum(self.start_pos) and turn == "computer":
            show_message_box("LOOOOSER", "YOU LOST. \nTRY AGAIN. \nSTARTING NEW GAME...", self.restart_game)

    def restart_game(self):
        self.pressed_buttons = {f"{_ + 1}{i}": 0 for _, j in enumerate(self.start_pos) for i in
                                range(1, int(j) + 1)}
        self.current_move = []
        for i in self.button_objects.values():
            i.setText("STONE")
            i.setStyleSheet(
                    widget_style_template.format(widget_type="QPushButton", font_size=20, border_color="black",
                                                 background_color=background_color,
                                                 text_color="black") +
                    hover_style_template.format(widget_type="QPushButton", hover_color=hover_color))

    def settings_button_clicked(self):
        settings_window = SettingsWindow(True)
        widget.setGeometry(screen_width, screen_height, 800, 600)
        widget.addWidget(settings_window)
        widget.setFixedSize(800, 600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def reset_btn_clicked(self):
        for i in self.current_move:
            self.button_objects[f"btn_{i}"].setText("STONE")
            self.button_objects[f"btn_{i}"].setStyleSheet("""
            QPushButton {
                    font: 20pt "MS Shell Dlg 2";
                    border-radius: 10px;
                    border: 2px solid black; 
                    background-color: rgb(136, 173, 102);
                }""")
        self.current_move = []

    def connect_current_pressed_btn(self):
        ans = self.pressed_buttons.copy()
        [ans.update({i: 1}) for i in self.current_move]
        return ans


class SettingsWindow(QMainWindow):
    def __init__(self, opened_from_game=False):
        super(SettingsWindow, self).__init__()
        self.ui = SettingsUi()
        self.ui.setupUi(self)

        self.ui.saved_label.hide()
        self.opened_from_game = opened_from_game
        self.default_settings = {
            "heaps_count": [3, 4, 5],
            "solo_mode": "False",
            "player_first_turn": "True"
        }
        self.load_settings()
        self.ui.exit_btn.clicked.connect(self.exit_btn_clicked)
        self.ui.save_btn.clicked.connect(self.save_btn_clicked)

    def load_settings(self):
        self.check_settings()
        f = json.loads(open(settings_json, "r").read())

        self.ui.heaps_input.setText(str(f["heaps_count"]))
        self.ui.solo_checkBox.setChecked(True if f["solo_mode"] == "True" else False)
        self.ui.turn_checkBox.setChecked(True if f["player_first_turn"] == "True" else False)

    def check_settings(self):

        try:
            f = json.loads(open(settings_json, "r").read())
        except Exception as e:
            print(e)
            file = open(settings_json, "w")
            file.write(json.dumps(self.default_settings, indent=4, ensure_ascii=False))
            return

        settings = {
            "heaps_count": f["heaps_count"] if "heaps_count" in f and f.get("heaps_count", "") != "" else
            self.default_settings["heaps_count"],
            "solo_mode": f["solo_mode"] if "solo_mode" in f else self.default_settings["solo_mode"],
            "player_first_turn": f["player_first_turn"] if "player_first_turn" in f else self.default_settings[
                "player_first_turn"]
        }

        file = open(settings_json, "w")
        file.write(json.dumps(settings, indent=4))
        file.close()

    def save_btn_clicked(self):
        f = open(settings_json, "w")

        try:
            heaps = [int(i) for i in self.ui.heaps_input.text()[1:-1].split(",")]
            if len(heaps) == 1:
                heaps = [3, 4, 5]
            heaps = [i if 6 >= i >= 0 else 6 for i in heaps]
            if len(heaps) > 9:
                heaps = heaps[:9]

        except Exception as e:
            print(e)
            heaps = [3, 4, 5]

        f.write(json.dumps({
            "heaps_count": heaps,
            "solo_mode": str(self.ui.solo_checkBox.isChecked()),
            "player_first_turn": str(self.ui.turn_checkBox.isChecked())
        }, indent=4))
        f.close()
        self.ui.saved_label.show()
        self.ui.saved_label.setText("Saved!")

    def exit_btn_clicked(self):
        if self.opened_from_game:
            game_ui = GameWindow()
            widget.addWidget(game_ui)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            main_window = NimGame()
            widget.addWidget(main_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == "__main__":
    create_settings_file = open(settings_json, "w")
    create_settings_file.write(json.dumps({"heaps_count": [3, 4, 5], "solo_mode": "False", "player_first_turn": "True"},
                                          indent=4))
    create_settings_file.close()

    app = QApplication(sys.argv)

    screen_width = app.desktop().screenGeometry().width() // 2 - 400
    screen_height = app.desktop().screenGeometry().height() // 2 - 300

    widget = QtWidgets.QStackedWidget()
    widget.addWidget(NimGame())
    widget.setWindowTitle("NimGame by Makcxim")
    widget.setWindowIcon(QtGui.QIcon(str(nim_icon)))
    widget.setGeometry(screen_width, screen_height, 800, 600)
    widget.setFixedSize(800, 600)
    widget.show()
    sys.exit(app.exec())
