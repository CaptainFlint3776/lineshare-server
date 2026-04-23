pythonfrom flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

lines = []

@app.route('/add_line', methods=['POST'])
def add_line():
    data = request.json
    line = {
        'user': data.get('user', 'anonymous'),
        'pair': data.get('pair', 'USDJPY'),
        'price': data.get('price', 0),
        'timeframe': data.get('timeframe', 'H1'),
        'timestamp': datetime.now().isoformat()
    }
    lines.append(line)
    return jsonify({'status': 'ok', 'line': line})

@app.route('/get_lines', methods=['GET'])
def get_lines():
    pair = request.args.get('pair', 'USDJPY')
    result = [l for l in lines if l['pair'] == pair]
    return jsonify({'lines': result})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
