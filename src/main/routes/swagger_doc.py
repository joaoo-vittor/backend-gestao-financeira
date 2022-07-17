from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/api/v1/doc"
API_URL = "/static/swagger.yaml"

swagger_bp = Blueprint("swagger_doc", __name__)


SWAGGER_BP = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "documentation to Account Service"}
)
