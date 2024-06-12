from PyQt6.QtWidgets import QMainWindow, QStackedLayout
from PyQt6.QtGui import QIcon

from ui.depot import DepotWindow
from ui.historique import HistoriqueWindow

from ui.login import LoginWindow
from ui.menu import MenuWindow
from ui.retrait import RetraitWindow
from ui.solde import SoldeWindow
from ui.transfert import TransfertWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        # self.setWindowIcon(QIcon('assets/logo.png'))
        self.setFixedSize(400, 600)
        self.user_identifiant = ''

        self.stackedWidget = QStackedLayout(self)
        
        self.loginWindow = LoginWindow(self)
        self.stackedWidget.addWidget(self.loginWindow)
        
        self.menuWindow = MenuWindow(self)
        self.stackedWidget.addWidget(self.menuWindow)
        
        self.depotWindow = DepotWindow(self)
        self.stackedWidget.addWidget(self.depotWindow)
        
        self.retraitWindow = RetraitWindow(self)
        self.stackedWidget.addWidget(self.retraitWindow)
        
        self.transfertWindow = TransfertWindow(self)
        self.stackedWidget.addWidget(self.transfertWindow)
        
        self.historiqueWindow = HistoriqueWindow(self)
        self.stackedWidget.addWidget(self.historiqueWindow)
        
        self.soldeWindow = SoldeWindow(self)
        self.stackedWidget.addWidget(self.soldeWindow)
        
        self.go_to_login()
        
    def go_to_login(self):
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.currentWidget().init_ui()
    def go_to_menu(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.currentWidget().init_ui()
    def go_to_depot(self):
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget.currentWidget().init_ui()
    def go_to_retrait(self):
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget.currentWidget().init_ui()
    def go_to_transfert(self):
        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget.currentWidget().init_ui()
    def go_to_historique(self):
        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget.currentWidget().init_ui()
    def go_to_solde(self):
        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget.currentWidget().init_ui()
