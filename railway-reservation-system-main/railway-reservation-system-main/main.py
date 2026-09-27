import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, 
    QPushButton, QLabel, QStackedWidget, QFrame
)
# Import your upgraded journey module
from journey import JourneyWidget, DARK_DASHBOARD_STYLE


class SidebarButton(QPushButton):
    """Custom styled sidebar button with active highlight support."""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #94A3B8;
                font-size: 14px;
                font-weight: 600;
                text-align: left;
                padding: 12px 18px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1E293B;
                color: #F8FAFC;
            }
            QPushButton:checked {
                background-color: #312E81;
                color: #818CF8;
            }
        """)


class RailwayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Rail Operations & Management Dashboard")
        self.resize(1100, 700)
        self.setStyleSheet(DARK_DASHBOARD_STYLE)

        # Central Wrapper Widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ---------------- 1. SIDEBAR PANEL ----------------
        sidebar = QFrame(self)
        sidebar.setStyleSheet("background-color: #0B1120; border-right: 1px solid #1E293B;")
        sidebar.setFixedWidth(240)
        
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(16, 24, 16, 24)
        sidebar_layout.setSpacing(8)

        # Brand / App Title
        brand_label = QLabel("🚆 RailPulse", sidebar)
        brand_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #6366F1; border: none; margin-bottom: 20px;")
        sidebar_layout.addWidget(brand_label)

        # Navigation Buttons
        self.btn_booking = SidebarButton("🎫  Book Ticket", sidebar)
        self.btn_schedules = SidebarButton("🕒  Train Schedules", sidebar)
        self.btn_history = SidebarButton("📜  Booking Ledger", sidebar)
        self.btn_analytics = SidebarButton("📊  Analytics (KPIs)", sidebar)

        self.nav_buttons = [self.btn_booking, self.btn_schedules, self.btn_history, self.btn_analytics]

        for btn in self.nav_buttons:
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        # System Status Indicator at bottom of sidebar
        status_box = QLabel("● System Operational", sidebar)
        status_box.setStyleSheet("color: #10B981; font-size: 12px; font-weight: bold; border: none;")
        sidebar_layout.addWidget(status_box)

        main_layout.addWidget(sidebar)

        # ---------------- 2. CONTENT STACK ----------------
        self.stacked_widget = QStackedWidget(self)
        
        # Instantiate Journey View Widget
        self.journey_page = JourneyWidget(self)
        self.stacked_widget.addWidget(self.journey_page)

        main_layout.addWidget(self.stacked_widget)

        # Connect Navigation Click Events
        self.btn_booking.clicked.connect(lambda: self.switch_tab(0, self.journey_page.show_booking_page))
        self.btn_schedules.clicked.connect(lambda: self.switch_tab(1, self.journey_page.show_trains_page))
        self.btn_history.clicked.connect(lambda: self.switch_tab(2, self.journey_page.show_history_page))
        self.btn_analytics.clicked.connect(lambda: self.switch_tab(3, None))

        # Set default active tab
        self.btn_booking.setChecked(True)

    def switch_tab(self, index, view_callback=None):
        """Switches active view tab and updates sidebar active button state."""
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)

        if view_callback:
            view_callback()
            self.stacked_widget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RailwayApp()
    window.show()
    sys.exit(app.exec())