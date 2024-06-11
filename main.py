"""Script entry point."""
import sys, os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from ui.app import MainWindow
from logger import LOGGER

basedir = os.path.dirname(__file__)

if __name__ == "__main__":
    LOGGER.success("App Executed")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, 'assets/logo_bg.jpg')))
    try:
        from ctypes import windll  # Only exists on Windows.
        myappid = 'ec2lt.banque.app.v1' # arbitrary string
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    
    # app.icon
    window = MainWindow()
    app.exec()