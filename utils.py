from PyQt6.QtWidgets import QInputDialog

def get_text_input(parent, title: str, label: str):
    text, ok = QInputDialog.getText(parent, title, label)
    return text, ok
