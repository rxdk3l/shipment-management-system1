from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFrame, QMenuBar, QMenu, QStatusBar,
    QAction, QMessageBox, QStyleFactory, QApplication
)
from PyQt6.QtGui import QKeySequence
from PyQt6.QtCore import Qt

from shipments import ShipmentsWidget
from products import ProductsWidget
from farmers import FarmersWidget
from manage import ManageWidget
from receipts import ReceiptsWidget

class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Shipment Management System")
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Sidebar
        sidebar = QFrame()
        sidebar.setFrameShape(QFrame.Shape.Box)
        sidebar.setMaximumWidth(200)
        sidebar_layout = QVBoxLayout()

        self.shipments_btn = QPushButton("Shipments")
        self.shipments_btn.clicked.connect(self.show_shipments)
        sidebar_layout.addWidget(self.shipments_btn)

        self.products_btn = QPushButton("Products")
        self.products_btn.clicked.connect(self.show_products)
        sidebar_layout.addWidget(self.products_btn)

        self.farmers_btn = QPushButton("Farmers")
        self.farmers_btn.clicked.connect(self.show_farmers)
        sidebar_layout.addWidget(self.farmers_btn)

        self.receipts_btn = QPushButton("Receipts")
        self.receipts_btn.clicked.connect(self.show_receipts)
        sidebar_layout.addWidget(self.receipts_btn)

        self.manage_btn = QPushButton("Manage")
        self.manage_btn.clicked.connect(self.show_manage)
        sidebar_layout.addWidget(self.manage_btn)

        sidebar_layout.addStretch()

        self.logout_btn = QPushButton("Logout")
        self.logout_btn.clicked.connect(self.close)
        sidebar_layout.addWidget(self.logout_btn)

        sidebar.setLayout(sidebar_layout)
        main_layout.addWidget(sidebar)

        self.content_area = QFrame()
        self.content_area.setFrameShape(QFrame.Shape.Box)
        self.content_layout = QVBoxLayout()
        self.content_area.setLayout(self.content_layout)
        main_layout.addWidget(self.content_area)

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        logout_action = QAction("Logout", self)
        logout_action.setShortcut(QKeySequence("Ctrl+L"))
        logout_action.triggered.connect(self.close)
        file_menu.addAction(logout_action)

        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        tools_menu = menubar.addMenu("Tools")
        new_shipment_action = QAction("New Shipment", self)
        new_shipment_action.setShortcut(QKeySequence("Ctrl+N"))
        new_shipment_action.triggered.connect(self.new_shipment)
        tools_menu.addAction(new_shipment_action)

        self.statusBar().showMessage("Ready")
        self.show_shipments()

    def clear_content(self):
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def show_shipments(self):
        self.clear_content()
        self.current_widget = ShipmentsWidget(self.db)
        self.content_layout.addWidget(self.current_widget)
        self.statusBar().showMessage("Shipments")

    def show_products(self):
        self.clear_content()
        self.current_widget = ProductsWidget(self.db)
        self.content_layout.addWidget(self.current_widget)
        self.statusBar().showMessage("Products")

    def show_farmers(self):
        self.clear_content()
        self.current_widget = FarmersWidget(self.db)
        self.content_layout.addWidget(self.current_widget)
        self.statusBar().showMessage("Farmers")

    def show_receipts(self):
        self.clear_content()
        self.current_widget = ReceiptsWidget(self.db)
        self.content_layout.addWidget(self.current_widget)
        self.statusBar().showMessage("Receipts")

    def show_manage(self):
        self.clear_content()
        self.current_widget = ManageWidget(self.db)
        self.content_layout.addWidget(self.current_widget)
        self.statusBar().showMessage("Stock Management")

    def new_shipment(self):
        if hasattr(self, 'current_widget') and isinstance(self.current_widget, ShipmentsWidget):
            self.current_widget.add_shipment()
