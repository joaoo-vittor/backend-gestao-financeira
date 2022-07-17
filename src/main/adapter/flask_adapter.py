from typing import Callable
from flask import Request
from src.presentation.helpers.http import HttpResponse, HttpRequest
from src.presentation.errors import HttpErrors


def flask_adapter(request: Request, callback: Callable) -> HttpResponse:
    """_summary_

    Args:
        request (Request): _description_
        callback (Callable): _description_

    Returns:
        HttpResponse: _description_
    """

    body = None
    query = None
    headers = None

    try:
        body = request.get_json()
        query = request.args.to_dict()
        headers = {i[0]: i[1] for i in request.headers.to_wsgi_list()}
    except Exception:
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["errors"]["status_code"], body=http_error
        )

    http_request = HttpRequest(header=headers, query=query, body=body)
    http_response = callback(http_request)

    return http_response
