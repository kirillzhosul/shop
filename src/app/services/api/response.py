#!env/bin/python
"""
    Merchandise shop API service API response.
    Provides class for API response.
"""

from typing import Dict

from flask import jsonify, request, Response

from .errors import api_get_error, ApiErrorType


class ApiResponse:
    """
    Base class for all API responses. Works as wrapper for API responses.
    Interface for better standart API.
    """

    @staticmethod
    def success(response: Dict, status_code=200) -> Response:
        """
        Returns succes API response with your body.
        :param response: Response body.
        :param status_code: HTTP Status code.
        :return: Final response.
        """
        response = {**response, **{
            # Standart API request information.
            "path": request.path,
            "status_code": status_code
        }}

        response = jsonify(response)
        response.status_code = status_code

        return response

    @staticmethod
    def error(api_error_type: ApiErrorType, *,
              field: str = "", message: str = "", detail: str = "") -> Response:
        """
        Returns API response as error from given API error type.
        :param api_error_type: Type of the error.
        :param field: Error field if allowed.
        :param message: Message for end-user.
        :param detail: Message for end-user.
        :return: Response JSON.
        """
        api_error = api_get_error(api_error_type, field=field, message=message, detail=detail)
        return ApiResponse.error_ext(api_error.status_code, api_error.code, api_error.type,
                                     api_error.message, api_error.detail)

    @staticmethod
    def error_ext(status_code: int, code: int, type: str, message: str, detail: str) -> Response:
        """
        Extended API error. Returns API response.
        :param code: API Error code.
        :param type: API Error type.
        :param message: Error message for end-user.
        :param detail: Error detail for end-user.
        :param status_code: HTTP Status code.
        :return: 
        """
        response = {
            "error": {
                # Standart error information.
                "code": code, "type": type,

                # End-user information messages.
                "message": message,
                "detail": detail
            },

            # Standart API request information.
            "path": request.path,
            "status_code": status_code
        }

        response = jsonify(response)
        response.status_code = status_code

        return response
