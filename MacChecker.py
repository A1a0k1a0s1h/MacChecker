import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit, QLabel

class MacAddressVendorChecker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MacTrace')
        self.setGeometry(100, 100, 440, 200)

        # MAC Address Input
        self.labelMac = QLabel('MAC Address:', self)
        self.labelMac.move(20, 20)
        self.inputMac = QLineEdit(self)
        self.inputMac.move(120, 20)
        self.inputMac.resize(200, 20)

        # Check Button
        self.btnCheck = QPushButton('Check', self)
        self.btnCheck.move(330, 20)
        self.btnCheck.clicked.connect(self.checkVendor)

        # Result Display
        self.resultDisplay = QTextEdit(self)
        self.resultDisplay.setReadOnly(True)
        self.resultDisplay.move(20, 60)
        self.resultDisplay.resize(360, 120)

        self.show()

    def checkVendor(self):
        mac_address = self.inputMac.text()
        url = f"https://api.macvendors.com/{mac_address}"
        try:
            response = requests.get(url)
            vendor = response.text
            self.resultDisplay.setText(vendor)
        except requests.RequestException as e:
            self.resultDisplay.setText("Error: " + str(e))

# Main loop
def main():
    app = QApplication(sys.argv)
    ex = MacAddressVendorChecker()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
