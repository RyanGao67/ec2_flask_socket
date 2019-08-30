from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

socketio = SocketIO()
def create_app():
    app = Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.secret_key = "secret"
    socketio.init_app(app, cors_allowed_origins="*")
    return app
import sys
sys.path.append('/home/tgao/tgao2019/socketio2019')
app = create_app()


# @socketio.on('my event', namespace='/test')
# def handleMessage(msg):
#     print("Message:" +msg['data'])
#     socketio.emit("my response", msg['data'], namespace='/chat')

@app.route('/', methods=['GET', "POST"])
def handleMessage():
    print("Message:")
    socketio.emit("my response", 'dd', namespace='/chat')
    return 'te'

if __name__ == '__main__':

    socketio.run(app, host="0.0.0.0", port=80)
