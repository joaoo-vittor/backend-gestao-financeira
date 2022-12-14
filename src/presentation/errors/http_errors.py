class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def error_422():
        """HTTP 422"""

        return {
            "errors": {"status_code": 422, "body": {"error": "Unprecessable Entity"}}
        }

    @staticmethod
    def error_401():
        """HTTP 401"""

        return {"errors": {"status_code": 401, "body": {"error": "Unauthorized"}}}

    @staticmethod
    def error_403():
        """HTTP 403"""

        return {"errors": {"status_code": 403, "body": {"error": "Forbidden"}}}

    @staticmethod
    def error_400():
        """HTTP 400"""

        return {"errors": {"status_code": 400, "body": {"error": "Bad Request"}}}

    @staticmethod
    def error_409():
        """HTTP 409"""

        return {"errors": {"status_code": 409, "body": {"error": "Conflict"}}}

    @staticmethod
    def error_500():
        """HTTP 409"""

        return {
            "errors": {"status_code": 500, "body": {"error": "Internal Server Error"}}
        }
