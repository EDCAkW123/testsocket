from flask import Flask, jsonify
from flask_socketio import SocketIO, emit

# HTTP сервер
http_app = Flask(__name__)

@http_app.route('/')
def index():
    return jsonify(message="HTTP сервер работает на порту 3000")

# WebSocket сервер
ws_app = Flask(__name__)
socketio = SocketIO(ws_app)

@socketio.on('connect')
def handle_connect():
    print("Клиент подключился к WebSocket")
    emit('response', {'message': 'Добро пожаловать в WebSocket сервер!'})

@socketio.on('message')
def handle_message(data):
    print(f"Получено сообщение: {data}")
    emit('response', {'message': f'Вы отправили: {data}'})

# Запуск серверов
if __name__ == '__main__':
    from multiprocessing import Process

    def run_http_server():
        http_app.run(host='0.0.0.0', port=3000)

    def run_ws_server():
        socketio.run(ws_app, host='0.0.0.0', port=5500, allow_unsafe_werkzeug=True)

    http_process = Process(target=run_http_server)
    ws_process = Process(target=run_ws_server)

    http_process.start()
    ws_process.start()

    http_process.join()
    ws_process.join()
