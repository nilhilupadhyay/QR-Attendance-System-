from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan_qr_code', methods=['POST'])
def scan_qr_code():
    qr_data = request.json['qr_data']
    # Process qr_data (e.g., store in Excel sheet, database)
    print('Scanned QR data:', qr_data)
    return jsonify({'message': 'QR code data received'})

if __name__ == '__main__':
    app.run(debug=True)
