#!env/bin/python
"""
    Merchandise shop API service API response.
    Provides class for API response.
"""

from flask import jsonify, request, Response

from .errors import api_get_error, ApiErrorType


class ApiResponse:
    """
    Base class for all API responses. Works as wrapper for API responses.
    Interface for better standart API.
    """

    @staticmethod
    def error(api_error_type: ApiErrorType) -> Response:
        """
        Returns API response as error from given API error type.
        :param api_error_type:
        :return: Response JSON.
        """
        api_error = api_get_error(api_error_type)

        response = {
            "error": {
                # Standart error information.
                "code": api_error.code, "type": api_error.type,

                # End-user information messages.
                "message": api_error.message,
                "detail": api_error.detail
            },

            # Standart API request information.
            "path": request.path,
            "status_code": api_error.status_code
        }

        response = jsonify(response)
        response.status_code = api_error.status_code

        return response
