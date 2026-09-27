# 🚆 RailPulse – Live Train Telemetry & Reservation System

RailPulse is a modern, full-stack railway reservation and live tracking web platform built with **Flask**, **Tailwind CSS**, and **Leaflet.js**. It provides users with a seamless experience from booking tickets across multiple coach classes to tracking train locations in real-time with smooth GPS-like telemetry animations.

---

## ✨ Key Features

- **🎫 End-to-End Ticket Booking:** Search train schedules, choose coach classes (1A, 2A, 3A, SL, CC) with dynamic pricing multipliers, input passenger details, and generate Electronic Reservation Slips (ERS).
- **🗺️ Interactive Live Telemetry Map:** Powered by **Leaflet.js** and OpenStreetMap, displaying complete geographic route lines and all journey stops.
- **🚆 Smooth Train Animation:** Features realistic linear interpolation (`requestAnimationFrame`) so the train glides smoothly along the route path rather than jumping across states.
- **📍 Journey Stops & Status Matrix:** Real-time schedule viewer displaying station arrival times alongside dynamic status badges (`RUNNING ON TIME`, `DELAYED`, `AHEAD`).
- **🚨 Automated Boarding Alerts:** Dynamic UI notification banners that trigger when the train approaches or reaches the user's boarding station.
- **🎨 Modern UI/UX:** Styled completely with **Tailwind CSS** featuring responsive glassmorphism/card layouts, micro-transitions, and interactive form states.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Jinja2 Templates
- **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6+), Leaflet.js
- **Routing & Interactivity:** Custom linear interpolation algorithms, DOM manipulation, responsive flex/grid layouts

---

## 📸 Application Preview

| Login & Authentication | Train Search & Selection |
| :---: | :---: |
| ![Login Page](login.png) | ![Train Search](train%20and%20coach.png) |

| Booking & Passenger Details | Payment Gateway Interface |
| :---: | :---: |
| ![Booking](book.png) | ![Payment](payment.png) |

| Generated Electronic Ticket | Live Map Telemetry & Tracking |
| :---: | :---: |
| ![Ticket](ticket.png) | ![Live Tracking](track.png) |

---

## 🚀 Getting Started Locally

Follow these steps to run RailPulse on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/PRANAV-MS25/railway-reservation-system.git]
   (https://github.com/PRANAV-MS25/railway-reservation-system.git)
   cd railway-reservation-system-main


   Install dependencies (Flask):

2. Bash
pip install flask
Run the application:

3. Bash
python app.py
Access in your browser:
Open http://127.0.0.1:5000 in your web browser.

👨‍💻 Author
M Pranav

GitHub: @PRANAV-MS25
