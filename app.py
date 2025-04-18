from flask import Flask, render_template
import os

app = Flask(__name__)

COUNTER_FILE = '/data/counter.txt'

def get_counter():
    try:
        with open(COUNTER_FILE, 'r') as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def save_counter(count):
    os.makedirs(os.path.dirname(COUNTER_FILE), exist_ok=True)
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(count))

@app.route('/')
def index():
    count = get_counter() + 1
    save_counter(count)
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    