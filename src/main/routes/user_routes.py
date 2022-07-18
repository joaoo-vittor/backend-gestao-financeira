from flask import jsonify, request, Blueprint
from src.main.adapter import flask_adapter
from src.main.composers import create_user_compose, login_user_compose


user_routes_bp = Blueprint("user_routes_bp", __name__)


@user_routes_bp.route("/user/register", methods=["POST"])
def register_user():
    response = flask_adapter(request, create_user_compose().handler)
    return jsonify(response.body), response.status_code


@user_routes_bp.route("/user/login", methods=["POST"])
def login_user():
    response = flask_adapter(request, login_user_compose().handler)
    return jsonify(response.body), response.status_code
