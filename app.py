from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def show_ip():
    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_ip = forwarded_for.split(',')[0].strip()  # Вибираємо першу IP-адресу
    return f"Ваша IP-адреса: {user_ip}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)