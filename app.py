from flask import Flask
from database import db
from database.config import Config
from routes.auth_routes import auth_bp
from routes.friend_routes import friends_bp
from routes.frontend_routes import frontend_bp
from flask_socketio import SocketIO
from chat_feature.chat_socket import register_chat_socket
from routes.chat_routes import chat_bp

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
socketio = SocketIO(app)


app.register_blueprint(auth_bp)
app.register_blueprint(frontend_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(friends_bp)

register_chat_socket(socketio)

with app.app_context():
    db.create_all()




if __name__ == "__main__":
    socketio.run(app, debug=True)