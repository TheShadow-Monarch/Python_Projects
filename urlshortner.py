import pyshorteners
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QTextEdit, QHBoxLayout, QMessageBox
from PyQt6.QtGui import QGuiApplication 

class URLWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("URL Shortener")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL to shorten")
        
        button_layout = QHBoxLayout()
        
        self.short_url_button = QPushButton("Shorten URL")
        self.short_url_button.clicked.connect(self.shorten_url)
        
        self.copy_url_button = QPushButton("Copy URL")
        self.copy_url_button.clicked.connect(self.copy_url)
        self.copy_url_button.setEnabled(False)  

        button_layout.addWidget(self.short_url_button)
        button_layout.addWidget(self.copy_url_button)
        button_layout.addStretch()

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Shortened URL will appear here")

        main_layout.addWidget(self.url_input)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_text)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def shorten_url(self):
        url = self.url_input.text()
        if not url:
            QMessageBox.warning(self, "Input Error", "Please enter a valid URL.")
            return
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            self.result_text.setText(short_url)
            self.copy_url_button.setEnabled(True)  # Enable copy button after shortening
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def copy_url(self):
        clipboard = QGuiApplication.clipboard()
        shortened_url = self.result_text.toPlainText()
        if shortened_url:
            clipboard.setText(shortened_url)
            QMessageBox.information(self, "Copied!", "URL copied to clipboard.")
        else:
            QMessageBox.warning(self, "Error", "No URL to copy.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = URLWindow()
    window.show()
    sys.exit(app.exec())