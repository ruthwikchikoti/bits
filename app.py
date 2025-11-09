from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/index.html')
def index_html():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/about.html')
def about():
    return send_from_directory(BASE_DIR, 'about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

