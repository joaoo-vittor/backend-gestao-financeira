from typing import Callable, Any
from flask import request, jsonify
from src.presentation.helpers.http import HttpResponse
from src.presentation.errors import HttpErrors


def tokens_is_required(route: Callable) -> Callable:
    def check_token(*args, **kwargs) -> Any:
        authentication_token = request.headers.get("Authentication")
        authorization_token = request.headers.get("Authorization")

        if not authentication_token:
            http_error = HttpErrors.error_401()
            http_response = HttpResponse(
                status_code=http_error["errors"]["status_code"],
                body=http_error,
            )
            return jsonify(http_response.body), http_response.status_code

        if not authorization_token:
            http_error = HttpErrors.error_401()
            http_response = HttpResponse(
                status_code=http_error["errors"]["status_code"],
                body=http_error,
            )
            return jsonify(http_response.body), http_response.status_code

        return route(*args, **kwargs)

    return check_token
