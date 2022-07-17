from flask import Flask
from src.main.routes import user_routes_bp, SWAGGER_URL, SWAGGER_BP


app = Flask(__name__)

app.register_blueprint(user_routes_bp, url_prefix="/api/v1")
app.register_blueprint(SWAGGER_BP, url_prefix=SWAGGER_URL)
