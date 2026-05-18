import sys
import webbrowser
from PyQt6.QtCore import Qt, QTime, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QStackedWidget, QMessageBox

from login import LoginWidget
from journey import JourneyWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Railway Reservation Management System")
        self.resize(1200, 750)
        
        self.statusBar().setStyleSheet("color: #EF4444; font-weight: bold; background-color: white; padding: 5px;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- Sidebar Layout Setup ---
        self.sidebar = QFrame(self)
        self.sidebar.setFixedWidth(230)
        self.sidebar.setStyleSheet("background-color: #1E293B;")
        nav_layout = QVBoxLayout(self.sidebar)
        nav_layout.setContentsMargins(15, 30, 15, 30)
        nav_layout.setSpacing(10)

        profile_icon = QLabel("👤", self.sidebar)
        profile_icon.setStyleSheet("font-size: 40px; color: white;")
        nav_layout.addWidget(profile_icon, alignment=Qt.AlignmentFlag.AlignCenter)

        btn_style = """
            QPushButton { background-color: transparent; border: none; color: white; text-align: left; padding: 12px; font-size: 14px; border-radius: 6px; }
            QPushButton:hover { background-color: #334155; }
            QPushButton:checked { background-color: #2563EB; font-weight: bold; }
            QPushButton:disabled { color: #475569; }
        """

        self.btn_nav_login = QPushButton("  Portal Login", self.sidebar)
        self.btn_nav_login.setCheckable(True)
        self.btn_nav_login.setStyleSheet(btn_style)
        self.btn_nav_login.setChecked(True)

        # Added New Dashboard Management Modules
        self.btn_nav_book = QPushButton("  Book Ticket", self.sidebar)
        self.btn_nav_book.setCheckable(True)
        self.btn_nav_book.setStyleSheet(btn_style)
        self.btn_nav_book.setEnabled(False)

        self.btn_nav_trains = QPushButton("  Trains Schedule", self.sidebar)
        self.btn_nav_trains.setCheckable(True)
        self.btn_nav_trains.setStyleSheet(btn_style)
        self.btn_nav_trains.setEnabled(False)

        self.btn_nav_history = QPushButton("  Booking History", self.sidebar)
        self.btn_nav_history.setCheckable(True)
        self.btn_nav_history.setStyleSheet(btn_style)
        self.btn_nav_history.setEnabled(False)

        self.btn_nav_about = QPushButton("  About Project", self.sidebar)
        self.btn_nav_about.setStyleSheet(btn_style)
        self.btn_nav_about.clicked.connect(self.on_actionAbout_triggered)

        self.btn_nav_bug = QPushButton("  Report Bug", self.sidebar)
        self.btn_nav_bug.setStyleSheet(btn_style)
        self.btn_nav_bug.clicked.connect(self.on_actionReport_Bug_triggered)

        self.btn_nav_quit = QPushButton("  Exit System", self.sidebar)
        self.btn_nav_quit.setStyleSheet(btn_style + " QPushButton { color: #F87171; }")
        self.btn_nav_quit.clicked.connect(self.on_actionQuit_triggered)

        nav_layout.addWidget(self.btn_nav_login)
        nav_layout.addWidget(self.btn_nav_book)
        nav_layout.addWidget(self.btn_nav_trains)
        nav_layout.addWidget(self.btn_nav_history)
        nav_layout.addWidget(self.btn_nav_about)
        nav_layout.addWidget(self.btn_nav_bug)
        nav_layout.addStretch()
        nav_layout.addWidget(self.btn_nav_quit)
        main_layout.addWidget(self.sidebar)

        # --- Content Panel System ---
        right_side = QWidget(self)
        right_layout = QVBoxLayout(right_side)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        right_side.setStyleSheet("background-color: #F1F5F9;")

        header_panel = QFrame(right_side)
        header_panel.setFixedHeight(70)
        header_panel.setStyleSheet("background-color: white; border-bottom: 1px solid #E2E8F0;")
        header_layout = QHBoxLayout(header_panel)
        header_layout.setContentsMargins(25, 0, 25, 0)

        header_title = QLabel("Central Railway Portal", header_panel)
        header_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #111827;")
        
        self.lbl_header_time = QLabel(self)
        self.lbl_header_time.setStyleSheet("font-size: 16px; color: #64748B; font-family: monospace; font-weight: bold;")
        header_layout.addWidget(header_title)
        header_layout.addStretch()
        header_layout.addWidget(self.lbl_header_time)
        right_layout.addWidget(header_panel)

        self.content_stack = QStackedWidget(right_side)
        self.content_stack.setContentsMargins(30, 30, 30, 30)

        self.login_page = LoginWidget(self, main_window=self)
        self.journey_manager = JourneyWidget(self) 

        self.content_stack.addWidget(self.login_page)       # Index 0
        self.content_stack.addWidget(self.journey_manager)   # Index 1
        self.content_stack.setCurrentWidget(self.login_page)

        right_layout.addWidget(self.content_stack)
        main_layout.addWidget(right_side)

        # Handle Routing Connections
        self.btn_nav_login.clicked.connect(lambda: self.switch_tab(0, self.btn_nav_login))
        self.btn_nav_book.clicked.connect(lambda: self.switch_tab(1, self.btn_nav_book, action="book"))
        self.btn_nav_trains.clicked.connect(lambda: self.switch_tab(1, self.btn_nav_trains, action="trains"))
        self.btn_nav_history.clicked.connect(lambda: self.switch_tab(1, self.btn_nav_history, action="history"))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_header_time)
        self.timer.start(1000)
        self.update_header_time()

    def switch_tab(self, index, active_button, action=None):
        self.btn_nav_login.setChecked(False)
        self.btn_nav_book.setChecked(False)
        self.btn_nav_trains.setChecked(False)
        self.btn_nav_history.setChecked(False)
        active_button.setChecked(True)
        
        if action == "book":
            self.journey_manager.show_booking_page()
        elif action == "trains":
            self.journey_manager.show_trains_page()
        elif action == "history":
            self.journey_manager.show_history_page()
            
        self.content_stack.setCurrentIndex(index)

    def unlock_dashboard(self):
        """Unlocks full dashboard access navigation tabs upon successful login verification"""
        self.btn_nav_book.setEnabled(True)
        self.btn_nav_trains.setEnabled(True)
        self.btn_nav_history.setEnabled(True)
        self.switch_tab(1, self.btn_nav_book, action="book")

    def update_header_time(self):
        self.lbl_header_time.setText(QTime.currentTime().toString("HH:mm:ss"))

    def on_actionAbout_triggered(self):
        QMessageBox.about(self, "About Project",
                          "This is an Advanced Railway Reservation Management System\n"
                          "Upgraded and refactored from legacy Qt C++ foundations.\n\n"
                          "Tools & Technologies used:\n"
                          "• Python 3\n"
                          "• PyQt6 / Modern UI Components\n\n"
                          "Lead Developer:\n"
                          "• PRANAV M")

    def on_actionQuit_triggered(self):
        QApplication.quit()

    def on_actionReport_Bug_triggered(self):
        url = "https://github.com/kHarshit/railway-ticketing-system/issues/new"
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())