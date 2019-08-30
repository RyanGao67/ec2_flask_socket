from flask_restful import Resource
from flask_socketio import SocketIO, send, emit
from server import app,socketio
class Reading(Resource):
    def get(self):
        print('hi from flask')
        socketio.emit('my response', 'cc',namespace='/chat')
