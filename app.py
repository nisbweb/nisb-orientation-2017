from flask import Flask, render_template,request, send_from_directory

from flask_socketio import SocketIO,send,emit

app = Flask(__name__)
#app.config['SECRET_KEY']='secret!'
socketio=SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def profile():
	return app.send_static_file('index.html')


@app.route('/<path:path>', methods=['GET', 'POST'])
def send_js(path):
    # return send_from_directory('', path)
    return app.send_static_file(path)

@socketio.on('eve1')
def handle_eve1(eve1):
	emit('news',"drskjgbkb")

@socketio.on('transit')
def handle_eve1(direction):
	emit('move',direction,broadcast=True)

if __name__ == '__main__':
	socketio.run(app,host='0.0.0.0')