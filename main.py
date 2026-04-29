from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
lines = []

@app.route('/add_line', methods=['POST', 'GET'])
def add_line():
    try:
        import json
        raw = request.data
        print("raw data: " + str(raw))
        data = json.loads(raw)
        print("parsed: " + str(data))
        line = {
            'user': str(data.get('user', 'anonymous')),
            'pair': str(data.get('pair', 'USDJPY')),
            'price': float(data.get('price', 0)),
            'timeframe': str(data.get('timeframe', 'H1')),
            'timestamp': str(datetime.now())
        }
        lines.append(line)
        print("received: " + str(line))
        return jsonify({'status': 'ok', 'line': line})
    except Exception as e:
        print("error: " + str(e))
        return jsonify({'error': str(e)}), 500
