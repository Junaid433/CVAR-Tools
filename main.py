from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget,
    QWidget, QVBoxLayout
)
import sys

from UI.Encryption import CVAREncryptor
from UI.Decryption import CVARDecryptor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PUBG Mobile CVAR Tool")

        tabs = QTabWidget()

        self.encrypt_tab = CVAREncryptor()
        self.decrypt_tab = CVARDecryptor()

        tabs.addTab(self.encrypt_tab, "Encrypt")
        tabs.addTab(self.decrypt_tab, "Decrypt")

        self.setCentralWidget(tabs)
        self.resize(700, 500)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
