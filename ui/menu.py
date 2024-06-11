import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout,QHBoxLayout, QLabel,QGridLayout 
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt

from logger import LOGGER


class MenuWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Menu Page")
        self.setFixedSize(400, 600)
        self.parentWindow = parent
        print(self.parentWindow.user_identifiant)
        
    def init_ui(self):
        pagelayout = QVBoxLayout(self)
        image_label = QLabel()
        pixmap = QPixmap('assets/logo.png')
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pagelayout.addWidget(image_label)
        
        title = QLabel()
        title.setText('Bienvenue')
        title.setObjectName("pageTitle")
        title.setWordWrap(True)
        title.setMargin(10)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pagelayout.addWidget(title)
        
        button_layout = QGridLayout(self)
        
        
        button = QPushButton()
        button.setText("Depot")
        button.setCheckable(True)
        button.clicked.connect(self.parentWindow.go_to_depot)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(button, 0, 0)
        
        button = QPushButton()
        button.setText("Retrait")
        button.setCheckable(True)
        button.clicked.connect(self.parentWindow.go_to_retrait)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(button, 0, 1)
        
        button = QPushButton()
        button.setText("Transfert")
        button.setCheckable(True)
        button.clicked.connect(self.parentWindow.go_to_transfert)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(button, 1, 0)
        
        button = QPushButton()
        button.setText("Solde")
        button.setCheckable(True)
        button.clicked.connect(self.parentWindow.go_to_solde)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(button, 1, 1)
        
        button = QPushButton()
        button.setText("Historique")
        button.setCheckable(True)
        button.clicked.connect(self.parentWindow.go_to_historique)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(button, 2, 0)
        
        button = QPushButton()
        button.setText("Quitter")
        button.setCheckable(True)
        button.clicked.connect(sys.exit)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(button, 2, 1)
        
        pagelayout.addLayout(button_layout)
        
        pagelayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(pagelayout)
        self.setStyleSheet("QLabel#pageTitle{ font-weight: 700;font-size:30px;}QWidget{background-color:#f6f6f6;color:#000}QPushButton {background-color: #253688;border: none;border-radius:10px;color: white;padding: 10px 30px;font-size: 15px;margin: 4px 2px;}QLineEdit{border:1px solid black ;color:#000;border-radius:10px;padding: 5px 5px;font-size: 15px;}") 

