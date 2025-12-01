import sys
import logging
from PyQt6.QtWidgets import QApplication, QStyleFactory
from PyQt6.QtCore import QStyleFactory
from database import Database
from login_dialog import LoginDialog
from main_window import MainWindow

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler('shipment_manager.log'), logging.StreamHandler(sys.stdout)]
    )

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    db = Database()

    login = LoginDialog(db)
    if login.exec() == QDialog.DialogCode.Accepted:
        window = MainWindow(db)
        window.showMaximized()
        sys.exit(app.exec())
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
