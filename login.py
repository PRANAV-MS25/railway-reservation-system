from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit, QPushButton

class LoginWidget(QWidget):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window 
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 50, 50, 50)
        
        card = QFrame(self)
        card.setFixedSize(400, 350)
        card.setStyleSheet("background-color: white; border-radius: 12px; border: 1px solid #E2E8F0;")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(30, 40, 30, 40)
        card_layout.setSpacing(15)
        
        title = QLabel("Secure Portal Login", card)
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1E293B; border: none;")
        card_layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.lineEdit_username = QLineEdit(card)
        self.lineEdit_username.setPlaceholderText("Username")
        self.lineEdit_username.setStyleSheet("padding: 10px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px; background: #F8FAFC; color: black;")
        
        self.lineEdit_password = QLineEdit(card)
        self.lineEdit_password.setPlaceholderText("Password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_password.setStyleSheet("padding: 10px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px; background: #F8FAFC; color: black;")
        
        self.nextPassenger = QPushButton("Login to System", card)
        self.nextPassenger.setStyleSheet("""
            QPushButton { background-color: #2563EB; color: white; font-weight: bold; padding: 12px; border-radius: 6px; border: none; font-size: 15px; }
            QPushButton:hover { background-color: #1D4ED8; }
        """)
        self.nextPassenger.clicked.connect(self.on_nextPassenger_clicked)
        
        card_layout.addWidget(self.lineEdit_username)
        card_layout.addWidget(self.lineEdit_password)
        card_layout.addWidget(self.nextPassenger)
        
        layout.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)

    def on_nextPassenger_clicked(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        
        if username == "Pranav0004" and password == "Bobby0004":
            self.lineEdit_username.clear()
            self.lineEdit_password.clear()
            self.main_window.statusBar().showMessage("Login successful!", 3000)
            self.main_window.unlock_dashboard() 
        else:
            self.main_window.statusBar().showMessage("username and password not correct. Please try again!", 3500)
            self.lineEdit_password.clear()