# file: stub_backend.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Kembalikan response statis sebagai stub
    return jsonify({"message": "Registrasi berhasil"}), 200

@app.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login berhasil"}), 200

if __name__ == '__main__':
    app.run(port=8000)
