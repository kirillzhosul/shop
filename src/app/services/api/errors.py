#!env/bin/python
"""
    Merchandise shop API service errors.
    Provides interface for API error raising.
"""
# TODO: Better handling of errors at level of `if`.

from enum import Enum, auto


class ApiErrorType(Enum):
    """API Error enumeration, provides type providing for `api_get_error`. """
    AUTH_REQUIRED = auto()  # User should be authenticated, but he don`t.


class ApiError:
    """API Error container, used in `response` API service as container. """
    def __init__(self, status_code: int, code: int, type: str, message: str, detail: str):
        """
        Constructor.
        :param status_code: HTTP Status code.
        :param code: API error code.
        :param type: API error type.
        :param message: Message for end-user.
        :param detail: Message for end-user.
        """
        self.status_code = status_code
        self.code = code
        self.type = type
        self.message = message
        self.detail = detail


def api_get_error(error_type: ApiErrorType) -> ApiError:
    """
    Returns API error container from error type.
    :param error_type: Type of the error.
    :return: ApiError container.
    """
    if error_type == ApiErrorType.AUTH_REQUIRED:
        return ApiError(
            status_code=401, code=1,
            type="AuthError",
            message="Авторизуйтесь для продолжения!",
            detail="Для выполнения данного метода, вы должны быть авторизованы!",
        )

    return ApiError(
        status_code=500, code=0,
        type="InternalServerError",
        message="Неизвестная ошибка!",
        detail="Данная ошибка не зависит от вас! Пожалуйста напишите в поддержку!",
    )
