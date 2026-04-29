from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
lines = []

@app.route('/add_line', methods=['POST', 'GET'])
def add_line():
    try:
        data = request.get_json(force=True, silent=True)
        if data is None:
            body = request.data.decode('utf-8')
            import json
            data = json.loads(body) if body else {}
        line = {
            'user': str(data.get('user', 'anonymous')),
            'pair': str(data.get('pair', 'USDJPY')),
            'price': float(data.get('price', 0)),
            'timeframe': str(data.get('timeframe', 'H1')),
            'timestamp': str(datetime.now())
        }
        lines.append(line)
        return jsonify({'status': 'ok', 'line': line})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
