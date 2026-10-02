import sys
    import webbrowser
    from PyQt6.QtCore import Qt, QTime, QTimer
           from PyQt6.QtWidgets import (
                                       QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                                       QPushButton, QLabel, QFrame, QStackedWidget, QMessageBox, QApplication
                                       )

# Import your journey/booking widget from your other file
# (Make sure journey.py has a class named JourneyWidget)
                                       from journey import JourneyWidget
                                       from login import LoginWidget # We will create this next to handle your inputs

                                       class MainWindow(QMainWindow):
                                       def __init__(self):
                                       super().__init__()
                                                        self.setWindowTitle("Railway Reservation Management System")
                                                                            self.resize(1200, 750)

# Initialize Status Bar (Replaces your C++ ui->statusBar)
                                                                                        self.statusBar().setStyleSheet("color: #EF4444; font-weight: bold; background-color: white; padding: 5px;")

# Container
                                                                                                       central_widget = QWidget(self)
                                                                                                                                self.setCentralWidget(central_widget)
                                                                                                                                main_layout = QHBoxLayout(central_widget)
                                                                                                                                                          main_layout.setContentsMargins(0, 0, 0, 0)
                                                                                                                                                                                         main_layout.setSpacing(0)

# --- Sidebar Navigation ---
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
                                                                                                                                                                                                                                                                                                                                                                                              QPushButton { background-color: transparent; border: none; color: white; text-align: left; padding: 12px; font-size: 15px; border-radius: 6px; }
QPushButton:hover { background-color: #334155; }
QPushButton:checked { background-color: #2563EB; font-weight: bold; }
QPushButton:disabled { color: #475569; }
"""

    self.btn_nav_login = QPushButton("  Portal Login", self.sidebar)
      self.btn_nav_login.setCheckable(True)
      self.btn_nav_login.setStyleSheet(btn_style)
      self.btn_nav_login.setChecked(True)

      self.btn_nav_dashboard = QPushButton("  Journey Booking", self.sidebar)
      self.btn_nav_dashboard.setCheckable(True)
      self.btn_nav_dashboard.setStyleSheet(btn_style)
      self.btn_nav_dashboard.setEnabled(False) # Locked until test/test login passes

# Action items mapped directly from your C++ menu actions
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
      nav_layout.addWidget(self.btn_nav_dashboard)
      nav_layout.addWidget(self.btn_nav_about)
      nav_layout.addWidget(self.btn_nav_bug)
      nav_layout.addStretch()
      nav_layout.addWidget(self.btn_nav_quit)

      main_layout.addWidget(self.sidebar)

# --- Right Side Workspace ---
      right_side = QWidget(self)
    right_layout = QVBoxLayout(right_side)
      right_layout.setContentsMargins(0, 0, 0, 0)
      right_layout.setSpacing(0)
      right_side.setStyleSheet("background-color: #F1F5F9;")

# Header Panel with System Clock
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

# --- Content Stack (Swaps between screens) ---
      self.content_stack = QStackedWidget(right_side)
      self.content_stack.setContentsMargins(30, 30, 30, 30)

      self.login_page = LoginWidget(self, main_window=self)
      self.booking_page = JourneyWidget(self)

      self.content_stack.addWidget(self.login_page)     # Index 0
      self.content_stack.addWidget(self.booking_page)   # Index 1
      self.content_stack.setCurrentWidget(self.login_page)

      right_layout.addWidget(self.content_stack)
      main_layout.addWidget(right_side)

# Sidebar navigation routing
      self.btn_nav_login.clicked.connect(lambda: self.switch_page(0, self.btn_nav_login))
      self.btn_nav_dashboard.clicked.connect(lambda: self.switch_page(1, self.btn_nav_dashboard))

# Realtime App Clock Trigger
      self.timer = QTimer(self)
      self.timer.timeout.connect(self.update_header_time)
      self.timer.start(1000)
      self.update_header_time()

      def switch_page(self, index, active_button):
    self.btn_nav_login.setChecked(False)
    self.btn_nav_dashboard.setChecked(False)
    active_button.setChecked(True)
    self.content_stack.setCurrentIndex(index)

    def unlock_dashboard(self):
    """Replaces the old hide/show window popup strategy cleanly inside the app frame"""
    self.btn_nav_dashboard.setEnabled(True)
    self.switch_page(1, self.btn_nav_dashboard)

    def update_header_time(self):
    self.lbl_header_time.setText(QTime.currentTime().toString("HH:mm:ss"))

# --- Your Original C++ Menu Actions Converted ---
    def on_actionAbout_triggered(self):
    QMessageBox.about(self, "About",
                      "This is a Railway Reservation System \n"
                      "developed for the OOP project.\n\n"
                      "Tools & Technologies used:\n"
                      "Python\n"
                      "PyQt6 / Qt\n\n"
                      "Developers:\n"
                      "Harshit Kumar (024)\n"
                      "Abhishek (002)\n"
                      "Aman Deep (008)")

    def on_actionQuit_triggered(self):
    QApplication.quit()

    def on_actionReport_Bug_triggered(self):
    url = "https://github.com/kHarshit/railway-ticketing-system/issues/new"
      webbrowser.open(url)