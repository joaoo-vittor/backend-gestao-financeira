from flask import Flask
from flask_jwt_extended import JWTManager
from src.main.routes import user_routes_bp, SWAGGER_URL, SWAGGER_BP
from src.settings import JWT_SECRET_KEY

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

JWTManager(app)

app.register_blueprint(user_routes_bp, url_prefix="/api/v1")
app.register_blueprint(SWAGGER_BP, url_prefix=SWAGGER_URL)
