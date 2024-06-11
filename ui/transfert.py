from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout,QMessageBox,QLineEdit, QLabel, QFormLayout
from PyQt6.QtGui import QPixmap, QCursor, QIntValidator
from PyQt6.QtCore import Qt
from logger import LOGGER
from controllers.client_controller import do_transaction

class TransfertWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Page de transfert")
        self.setFixedSize(400, 600)
        self.parentWindow = parent
        
    def init_ui(self):
        pagelayout = QVBoxLayout(self)
        
        title = QLabel()
        title.setText('Operation de transfert de fonds')
        title.setObjectName("pageTitle")
        title.setWordWrap(True)
        title.setMargin(10)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pagelayout.addWidget(title)
        
        image_label = QLabel()
        pixmap = QPixmap('assets/logo.png')
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pagelayout.addWidget(image_label)
        
        fbox = QFormLayout(self)
        self.amount = QLineEdit()
        self.pin = QLineEdit()
        self.reciever_account_num = QLineEdit()
        self.amount.setValidator(QIntValidator(0, 1000000000))
        # self.amount.setInputMask("9")
        fbox.addRow(QLabel("Code Pin"), self.pin)
        fbox.addRow(QLabel("Montant"), self.amount)
        fbox.addRow(QLabel("Numero compte beneficiaire"), self.reciever_account_num)
        fbox.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        pagelayout.addLayout(fbox)
        
        button = QPushButton()
        button.setText("Valider")
        button.setCheckable(True)
        button.clicked.connect(self.transaction_compte)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        pagelayout.addWidget(button)
        
        button = QPushButton()
        button.setText("Retour au menu")
        button.setCheckable(True)
        button.clicked.connect(self.parentWindow.go_to_menu)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        pagelayout.addWidget(button)
        
        pagelayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(pagelayout)
        self.setStyleSheet("QLabel#pageTitle{ font-weight: 700;font-size:20px;}QWidget{background-color:#f6f6f6;color:#000}QPushButton {background-color: #253688;border: none;border-radius:10px;color: white;padding: 10px 30px;font-size: 15px;margin: 4px 2px;}QLineEdit{border:1px solid black ;color:#000;border-radius:10px;padding: 5px 5px;font-size: 15px;}")
    def transaction_compte(self):
        transaction_solde = do_transaction(self.parentWindow.user_identifiant, self.pin.text(),int(self.amount.text()), self.reciever_account_num.text())
        if(transaction_solde.login_done):
            if(transaction_solde.transfert_done):
                QMessageBox.information(self, "Transaction effectué",transaction_solde.message_transfert,buttons=QMessageBox.StandardButton.Ok,defaultButton=QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.critical(self, "Erreur", transaction_solde.message_transfert,buttons=QMessageBox.StandardButton.Ok,defaultButton=QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.critical(self,"Erreur",transaction_solde.message_login,buttons=QMessageBox.StandardButton.Ok,defaultButton=QMessageBox.StandardButton.Ok)
        self.pin.setText('')
        self.amount.setText('')
        self.reciever_account_num.setText('')