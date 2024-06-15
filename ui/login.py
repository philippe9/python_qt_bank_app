from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout,QMessageBox,QLineEdit, QLabel, QFormLayout
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt
from controllers.client_controller import login_customer
from logger import LOGGER

class LoginWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setFixedSize(400, 600)
        self.parentWindow = parent

    def init_ui(self):
        pagelayout = QVBoxLayout(self)
        image_label = QLabel()
        pixmap = QPixmap('assets/logo.png')
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pagelayout.addWidget(image_label)

        title = QLabel()
        title.setText('Application de gestion de banque EC2LT')
        title.setObjectName("pageTitle")
        title.setWordWrap(True)
        title.setMargin(10)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pagelayout.addWidget(title)
        
        fbox = QFormLayout(self)
        self.user_name = QLineEdit()
        self.pin = QLineEdit()
        
        fbox.addRow(QLabel("Nom d'utilisateur"), self.user_name)
        fbox.addRow(QLabel("Code Pin"), self.pin)
        fbox.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        pagelayout.addLayout(fbox)
        
        button = QPushButton()
        button.setText("CONNEXION")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        pagelayout.addWidget(button)
        
        pagelayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(pagelayout)
        self.setStyleSheet("QLabel#pageTitle{ font-weight: 700;font-size:20px;}QWidget{background-color:#f6f6f6;color:#000}QPushButton {background-color: #253688;border: none;border-radius:10px;color: white;padding: 10px 30px;font-size: 15px;margin: 4px 2px;}QLineEdit{border:1px solid black ;color:#000;border-radius:10px;padding: 5px 5px;font-size: 15px;}")
    def the_button_was_clicked(self):
        user = login_customer(self.user_name.text(),self.pin.text())
        if(user):
            self.parentWindow.user_identifiant = user.identifiant
            self.parentWindow.go_to_menu()
        else:
            QMessageBox.critical(self,"Erreur","Identifiants incorrects.",buttons=QMessageBox.StandardButton.Ok,defaultButton=QMessageBox.StandardButton.Ok)
            
