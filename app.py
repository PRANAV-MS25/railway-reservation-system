from flask import Flask, render_template, request, session, redirect, url_for, send_file
import random
import datetime
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = "railpulse_complete_flow_2026"

COACH_RATES = {
    "1AC": {"name": "First AC (1AC)", "multiplier": 2.5},
    "2AC": {"name": "Second AC (2AC)", "multiplier": 1.8},
    "3AC": {"name": "Third AC (3AC)", "multiplier": 1.3},
    "Sleeper": {"name": "Sleeper (SL)", "multiplier": 1.0},
    "General": {"name": "General (GEN)", "multiplier": 0.6}
}

TRAINS_DB = [
    {
        "train_no": "12627",
        "train_name": "Karnataka Express",
        "departure": "19:20",
        "arrival": "06:45 (+2 Days)",
        "base_fare": 1200,
    }
]

# Step 1: Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_values = list(request.form.values())
        session['user'] = form_values[0] if form_values else "Passenger"
        return redirect(url_for('home'))
    return render_template('login.html')

# Step 2: Home Dashboard
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_values = list(request.form.values())
        if form_values:
            session['user'] = form_values[0]
            
    if 'user' not in session:
        return redirect(url_for('login'))
        
    return render_template('home.html', user=session.get('user'))

# Step 3 & 4: Destination From-To Search
@app.route('/search-trains', methods=['POST'])
def search_trains():
    session['from_station'] = request.form.get('from_station')
    session['to_station'] = request.form.get('to_station')
    session['journey_date'] = request.form.get('journey_date')
    return render_template('trains.html', trains=TRAINS_DB, coaches=COACH_RATES)

# Step 5 & 6: Train & Coach Selection
@app.route('/passenger', methods=['POST'])
def passenger():
    session['train_no'] = request.form.get('train_no')
    session['train_name'] = request.form.get('train_name')
    
    coach_code = request.form.get('coach_type')
    coach_info = COACH_RATES.get(coach_code, COACH_RATES['Sleeper'])
    base_fare = float(request.form.get('base_fare', 1200))
    
    session['coach_type'] = coach_info['name']
    session['calculated_fare'] = int(base_fare * coach_info['multiplier'])
    return render_template('passenger.html')

# Step 7: Payment & Ticket Generation Route
@app.route('/process-payment', methods=['POST', 'GET'])
@app.route('/ticket', methods=['POST', 'GET'])
def ticket_or_payment():
    if request.method == 'POST':
        session['passenger_name'] = request.form.get('passenger_name')
        session['passenger_age'] = request.form.get('passenger_age')
        session['passenger_gender'] = request.form.get('passenger_gender')
        session['berth_preference'] = request.form.get('berth_preference')
        session['payment_mode'] = request.form.get('payment_mode', 'UPI / NetBanking')
        
        # Generate PNR and timestamp if not already present
        if 'pnr' not in session:
            session['pnr'] = f"28{random.randint(10000000, 99999999)}"
        session['booking_time'] = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")

    ticket_data = {
        "pnr": session.get('pnr'),
        "train_no": session.get('train_no'),
        "train_name": session.get('train_name'),
        "from_station": session.get('from_station'),
        "to_station": session.get('to_station'),
        "journey_date": session.get('journey_date'),
        "coach_type": session.get('coach_type'),
        "passenger_name": session.get('passenger_name'),
        "passenger_age": session.get('passenger_age'),
        "passenger_gender": session.get('passenger_gender'),
        "berth_preference": session.get('berth_preference'),
        "payment_mode": session.get('payment_mode'),
        "calculated_fare": session.get('calculated_fare'),
        "booking_time": session.get('booking_time')
    }
    
    return render_template('ticket.html', ticket=ticket_data)

# Live Train Tracking Route
@app.route('/tracking')
def tracking():
    if 'pnr' not in session:
        return redirect(url_for('home'))
        
    ticket_data = {
        "pnr": session.get('pnr'),
        "train_no": session.get('train_no', '12627'),
        "train_name": session.get('train_name', 'Karnataka Express'),
        "from": session.get('from_station', 'KSR Bengaluru (SBC)'),
        "to": session.get('to_station', 'New Delhi (NDLS)')
    }
    
    stops = [
        {"name": "KSR Bengaluru (SBC)", "lat": 12.9784, "lng": 77.5700, "time": "19:20"},
        {"name": "Dharmavaram Jn", "lat": 14.4132, "lng": 77.7157, "time": "21:55"},
        {"name": "Secunderabad Jn", "lat": 17.4340, "lng": 78.5010, "time": "06:10"},
        {"name": "Nagpur Jn", "lat": 21.1458, "lng": 79.0882, "time": "18:30"},
        {"name": "New Delhi (NDLS)", "lat": 28.6139, "lng": 77.2090, "time": "06:45"}
    ]
    
    return render_template('tracking.html', ticket=ticket_data, stops=stops)

# Step 8: Receive Ticket as a PDF Download
@app.route('/download-ticket-pdf')
def download_ticket_pdf():
    if 'pnr' not in session:
        return redirect(url_for('home'))
        
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 750, "INDIAN RAILWAYS - ELECTRONIC RESERVATION SLIP (ERS)")
    
    p.setFont("Helvetica", 10)
    p.drawString(50, 730, f"PNR No: {session.get('pnr')}")
    p.drawString(350, 730, f"Booking Time: {session.get('booking_time')}")
    
    p.line(50, 720, 560, 720)
    
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 695, "Train Journey Details")
    p.setFont("Helvetica", 10)
    p.drawString(50, 675, f"Train: {session.get('train_no')} - {session.get('train_name')}")
    p.drawString(50, 655, f"From: {session.get('from_station')}   -->   To: {session.get('to_station')}")
    p.drawString(50, 635, f"Date of Journey: {session.get('journey_date')} | Coach Class: {session.get('coach_type')}")
    
    p.line(50, 620, 560, 620)
    
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 595, "Passenger Manifest")
    p.setFont("Helvetica", 10)
    p.drawString(50, 575, f"Name: {session.get('passenger_name')}")
    p.drawString(50, 555, f"Age/Gender: {session.get('passenger_age')} yrs / {session.get('passenger_gender')}")
    p.drawString(50, 535, f"Berth Preference: {session.get('berth_preference')} | Status: CNF / B3 - 21")
    
    p.line(50, 520, 560, 520)
    
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 495, "Payment & Fare Summary")
    p.setFont("Helvetica", 10)
    p.drawString(50, 475, f"Payment Mode: {session.get('payment_mode')}")
    p.drawString(50, 455, f"Total Fare Paid: ₹{session.get('calculated_fare')}")
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    
    return send_file(buffer, as_attachment=True, download_name=f"Ticket_{session.get('pnr')}.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)