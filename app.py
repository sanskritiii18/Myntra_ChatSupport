from flask import Flask
from database import db
from database.config import Config
from routes.auth_routes import auth_bp
from routes.frontend_routes import frontend_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(frontend_bp)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)