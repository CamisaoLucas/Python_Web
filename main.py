from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Funcionalidade de Enviar mensagem
@socketio.on('message')
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# Criar a nossa 1ª página = 1ª rota
@app.route('/')
def homepage():
    return render_template('index.html')
app.add_url_rule('/', endpoint='index')

# Roda o nosso aplicativo
socketio.run(app, host='localhost')