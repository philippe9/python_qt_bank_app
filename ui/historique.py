from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout,QGridLayout,QLineEdit, QLabel, QFormLayout, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QColor, QCursor, QIntValidator
from PyQt6.QtCore import Qt
from logger import LOGGER
from controllers.client_controller import list_user_transaction, login_customer

class HistoriqueWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Page d'historisque")
        self.setFixedSize(950, 600)
        self.parentWindow = parent
        
    def init_ui(self):
        self.pagelayout = QVBoxLayout(self)
        
        title = QLabel()
        title.setText("Page d'historisque")
        title.setObjectName("pageTitle")
        title.setWordWrap(True)
        title.setMargin(10)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pagelayout.addWidget(title)
        
        form_layout = QGridLayout(self)
        
        fbox = QFormLayout(self)
        self.pin = QLineEdit()
        fbox.addRow(QLabel("Code Pin"), self.pin)
        fbox.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        form_layout.addLayout(fbox,0,0)
        
        fbox = QFormLayout(self)
        self.nombre_transactions = QLineEdit()
        self.nombre_transactions.setValidator(QIntValidator(0, 1000000000))
        fbox.addRow(QLabel("Nombre de transactions(10 par defaut)"), self.nombre_transactions)
        fbox.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        form_layout.addLayout(fbox,0,1)
        
        self.pagelayout.addLayout(form_layout)
        
        button_layout = QGridLayout(self)
        
        button = QPushButton()
        button.setText("Lister")
        button.setCheckable(True)
        button.clicked.connect(self.get_user_trx)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(button, 0, 0)
        
        button = QPushButton()
        button.setText("Retour")
        button.setCheckable(True)
        button.clicked.connect(self.parentWindow.go_to_menu)
        button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(button, 0, 1)
        self.pagelayout.addLayout(button_layout)

        self.pagelayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.pagelayout)
        self.setStyleSheet("QLabel#pageTitle{ font-weight: 700;font-size:20px;}QWidget{background-color:#f6f6f6;color:#000}QPushButton {background-color: #253688;border: none;border-radius:10px;color: white;padding: 10px 30px;font-size: 15px;margin: 4px 2px;}QLineEdit{border:1px solid black ;color:#000;border-radius:10px;padding: 5px 5px;font-size: 15px;}")
        self.user_trx = []
        self.table = QTableWidget(0,6)
        self.table.setHorizontalHeaderLabels(["Montant", "Type", "Compte emmeteur","Compte recepteur", "Date de l'operation","Mat operation"])
        self.table.setEnabled(False)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.pagelayout.addWidget(self.table)
       
    def get_user_trx(self):
        nb = self.nombre_transactions.text()
        trxs = list_user_transaction(self.parentWindow.user_identifiant, self.pin.text(), 10 if nb == '' else int(nb) )
        if(trxs):
            self.user_trx = trxs
            self.current_user = login_customer(self.parentWindow.user_identifiant, self.pin.text())
            self.update_ui_trx()
        else:
            QMessageBox.critical(self,"Erreur","Identifiants incorrect",buttons=QMessageBox.StandardButton.Ok,defaultButton=QMessageBox.StandardButton.Ok)
        self.pin.setText('')
    def update_ui_trx(self):
        if(len(self.user_trx) > 0):
            self.pagelayout.removeWidget(self.table)
            self.table = QTableWidget(len(self.user_trx), 6)
            self.table.setEnabled(False)
            self.table.setHorizontalHeaderLabels(["Montant", "Type", "Compte emmeteur","Compte recepteur", "Date de l'operation","Mat operation"])
            for i, item in enumerate(self.user_trx):
                
                self.table.setItem(i, 0, QTableWidgetItem(f"{str(item.montant)} FCFA"))
                self.table.setItem(i, 1, QTableWidgetItem(item.type))
                self.table.setItem(i, 2 , QTableWidgetItem(item.compte_emmeteur_obj.nom))
                self.table.setItem(i, 3 , QTableWidgetItem(item.compte_recepteur_obj.nom))
                self.table.setItem(i, 4 , QTableWidgetItem(item.date.strftime('%a %d/%m/%Y , %H:%M:%S')))
                self.table.setItem(i, 5 , QTableWidgetItem(item.matricule_transaction ))
                # print()
                self.table.setColumnWidth(0, 150)
                self.table.setColumnWidth(1, 150)
                self.table.setColumnWidth(2, 150)
                self.table.setColumnWidth(3, 150)
                self.table.setColumnWidth(4, 150)
                self.table.setColumnWidth(5, 150)
            for i, item in enumerate(self.user_trx):
                if item.type == 'DEPOT':
                    self.table.item(i, 1).setBackground(QColor(0, 200, 0))
                if item.type == 'RETRAIT':
                    self.table.item(i, 1).setBackground(QColor(200, 100, 100, 50))
                if item.type == 'TRANSACTION':
                    if item.compte_recepteur_obj.identifiant == self.current_user.identifiant:
                        self.table.item(i, 1).setBackground(QColor(0, 200, 0))
                    else:
                        self.table.item(i, 1).setBackground(QColor(200, 100, 100, 50))
                    
        self.pagelayout.addWidget(self.table)