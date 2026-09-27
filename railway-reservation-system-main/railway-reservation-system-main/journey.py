from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QPushButton, QFrame, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox

class JourneyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        # In-memory database for tracking live records
        self.history_records = [
            ["PRANAV M", "New Delhi (NDLS)", "Mumbai Central (MMCT)", "2026-06-01", "₹1,250"],
            ["PRANAV M", "Pune Junction (PUNE)", "KSR Bengaluru (SBC)", "2026-06-15", "₹950"]
        ]
        
        # Pricing matrix dictionary between stations
        self.fare_matrix = {
            "New Delhi (NDLS)": {"Mumbai Central (MMCT)": 1250, "Howrah Junction (HWH)": 1400, "KSR Bengaluru (SBC)": 2100, "Pune Junction (PUNE)": 1150},
            "Mumbai Central (MMCT)": {"New Delhi (NDLS)": 1250, "Howrah Junction (HWH)": 1650, "KSR Bengaluru (SBC)": 980, "Pune Junction (PUNE)": 200},
            "Howrah Junction (HWH)": {"New Delhi (NDLS)": 1400, "Mumbai Central (MMCT)": 1650, "KSR Bengaluru (SBC)": 1850, "Pune Junction (PUNE)": 1500},
            "KSR Bengaluru (SBC)": {"New Delhi (NDLS)": 2100, "Mumbai Central (MMCT)": 980, "Howrah Junction (HWH)": 1850, "Pune Junction (PUNE)": 750},
            "Pune Junction (PUNE)": {"New Delhi (NDLS)": 1150, "Mumbai Central (MMCT)": 200, "Howrah Junction (HWH)": 1500, "KSR Bengaluru (SBC)": 750}
        }
        
        self.stations = ["-- Select Station --", "New Delhi (NDLS)", "Mumbai Central (MMCT)", "Howrah Junction (HWH)", "KSR Bengaluru (SBC)", "Pune Junction (PUNE)"]
        
        # Render the initial screen wrapper
        self.show_booking_page()

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    # --- VIEW 1: BOOKING SCREEN ---
    def show_booking_page(self):
        self.clear_layout()
        
        card = QFrame(self)
        card.setStyleSheet("background-color: white; border-radius: 12px; border: 1px solid #E2E8F0;")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(40, 40, 40, 40)
        
        form_grid = QGridLayout()
        form_grid.setSpacing(20)
        
        lbl_style = "font-size: 15px; font-weight: bold; color: #334155; border: none;"
        input_style = "padding: 8px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 14px; background-color: white; color: black;"
        
        # Form Controls
        form_grid.addWidget(QLabel("Passenger Name:", card), 0, 0)
        self.lineEdit_name = QLineEdit(card)
        self.lineEdit_name.setStyleSheet(input_style)
        form_grid.addWidget(self.lineEdit_name, 0, 1)
        
        form_grid.addWidget(QLabel("Source Station:", card), 1, 0)
        self.comboBox_from = QComboBox(card)
        self.comboBox_from.addItems(self.stations)
        self.comboBox_from.setStyleSheet(input_style)
        self.comboBox_from.currentTextChanged.connect(self.calculate_live_fare)
        form_grid.addWidget(self.comboBox_from, 1, 1)
        
        form_grid.addWidget(QLabel("Destination Station:", card), 2, 0)
        self.comboBox_to = QComboBox(card)
        self.comboBox_to.addItems(self.stations)
        self.comboBox_to.setStyleSheet(input_style)
        self.comboBox_to.currentTextChanged.connect(self.calculate_live_fare)
        form_grid.addWidget(self.comboBox_to, 2, 1)
        
        form_grid.addWidget(QLabel("Journey Date:", card), 3, 0)
        self.dateEdit = QDateEdit(card)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setStyleSheet(input_style)
        form_grid.addWidget(self.dateEdit, 3, 1)
        
        # Estimated Cost UI Display Block
        form_grid.addWidget(QLabel("Estimated Fare:", card), 4, 0)
        self.lbl_fare_display = QLabel("₹0", card)
        self.lbl_fare_display.setStyleSheet("font-size: 18px; font-weight: bold; color: #16A34A; border: none;")
        form_grid.addWidget(self.lbl_fare_display, 4, 1)
        
        # Clean labels stylesheet application safely
        for i in range(form_grid.count()):
            w = form_grid.itemAt(i).widget()
            if isinstance(w, QLabel) and w != self.lbl_fare_display:
                w.setStyleSheet(lbl_style)

        self.btn_book = QPushButton("Confirm Booking", card)
        self.btn_book.setStyleSheet("background-color: #2563EB; color: white; font-weight: bold; padding: 12px 40px; border-radius: 6px; border: none; font-size: 15px;")
        self.btn_book.clicked.connect(self.process_booking)
        
        card_layout.addLayout(form_grid)
        card_layout.addSpacing(25)
        card_layout.addWidget(self.btn_book, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)

    def calculate_live_fare(self):
        frm = self.comboBox_from.currentText()
        to = self.comboBox_to.currentText()
        if frm in self.fare_matrix and to in self.fare_matrix[frm]:
            self.lbl_fare_display.setText(f"₹{self.fare_matrix[frm][to]}")
        else:
            self.lbl_fare_display.setText("₹0")

    def process_booking(self):
        name = self.lineEdit_name.text().strip()
        frm = self.comboBox_from.currentText()
        to = self.comboBox_to.currentText()
        date = self.dateEdit.date().toString("yyyy-MM-dd")
        cost = self.lbl_fare_display.text()
        
        if not name or frm == self.stations[0] or to == self.stations[0]:
            QMessageBox.warning(self, "Validation Error", "Please provide a valid passenger name and route.")
            return
        if frm == to:
            QMessageBox.warning(self, "Route Error", "Source and Destination cannot be the same station.")
            return
            
        self.history_records.append([name, frm, to, date, cost])
        QMessageBox.information(self, "Success", f"Ticket issued successfully for {name}!\nTotal Charged: {cost}")
        self.show_history_page()

    # --- VIEW 2: TRAINS LIST SCHEDULE ---
    def show_trains_page(self):
        self.clear_layout()
        title = QLabel("Available Route Trains & Schedules")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #1E293B; margin-bottom: 10px;")
        self.layout.addWidget(title)
        
        table = QTableWidget(6, 4)
        table.setHorizontalHeaderLabels(["Train Name / No.", "Route Sector", "Departure Time", "Base Class Fare"])
        table.setStyleSheet("background-color: white; gridline-color: #E2E8F0; color: black;")
        
        schedules = [
            ["Rajdhani Express (12424)", "NDLS ➔ HWH", "16:55", "₹1,400"],
            ["Shatabdi Express (12002)", "NDLS ➔ PUNE", "06:00", "₹1,150"],
            ["Duronto Express (12260)", "MMCT ➔ NDLS", "23:15", "₹1,250"],
            ["Silicon City SF (22691)", "SBC ➔ PUNE", "20:00", "₹750"],
            ["Deccan Queen (12124)", "PUNE ➔ MMCT", "07:15", "₹200"],
            ["Intercity SF Express", "MMCT ➔ SBC", "09:30", "₹980"]
        ]
        
        for row, data in enumerate(schedules):
            for col, val in enumerate(data):
                item = QTableWidgetItem(val)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                table.setItem(row, col, item)
                
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(table)

    # --- VIEW 3: BOOKING HISTORY LEDGER ---
    def show_history_page(self):
        self.clear_layout()
        title = QLabel("System Ticket Booking History Ledger")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #1E293B; margin-bottom: 10px;")
        self.layout.addWidget(title)
        
        table = QTableWidget(len(self.history_records), 5)
        table.setHorizontalHeaderLabels(["Passenger Name", "Source From", "Destination Target", "Date", "Fare Cleared"])
        table.setStyleSheet("background-color: white; gridline-color: #E2E8F0; color: black;")
        
        for row, data in enumerate(self.history_records):
            for col, val in enumerate(data):
                item = QTableWidgetItem(val)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                table.setItem(row, col, item)
                
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(table)