from pathlib import Path

data_folder = Path("data")
main_background = data_folder / "main_background.png"
main_gif = data_folder / "main_ui.gif"

settings_background = data_folder / "settings_background.jpg"
settings_json = data_folder / "settings.json"

game_background = data_folder / "game_background.jpg"

nim_icon = data_folder / "icon.webp"


widget_style_template = """
    {widget_type} {{
        font: {font_size}pt "MS Shell Dlg 2";
        border-radius: 20px;
        border: 2px solid {border_color};
        background-color: {background_color};
        color: {text_color};
    }}
"""

hover_style_template = """
    {widget_type}:hover {{
        border: 3px solid {hover_color};
        background-color: {hover_color};
    }}
"""
