#!env/bin/python
"""
    Merchandise shop API service errors.
    Provides interface for API error raising.
"""
# TODO: Better handling of errors at level of `if`.
# TODO: Add field error reporting in final response.

from enum import Enum, auto


class ApiErrorType(Enum):
    """API Error enumeration, provides type providing for `api_get_error`. """
    AUTH_REQUIRED = auto()  # User should be authenticated, but he don`t.
    AUTH_DISSALOWED = auto()  # User should be not authenticated, but he is.
    AUTH_ALREADY_EXISTS = auto()  # User tried to register account with already taken data.
    AUTH_FAILED = auto()  # User auth failed because of incorrect credentials.
    AUTH_PASSWORD_CONFIRMATION_MISMATCH = auto()  # Password and password confirmation not the same.

    FIELD_REQUIRED = auto()  # Required field is not found.
    FIELD_INVALID = auto()  # Invalid field passed. (Almost general error).
    FIELD_TOO_SHORT = auto()
    FIELD_TOO_LONG = auto()

    PAYMENT_ERROR = auto()  # When there is some error in payment handling.


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


def api_get_error(error_type: ApiErrorType, *,
                  field: str = "", message: str = "", detail: str = "") -> ApiError:
    """
    Returns API error container from error type.
    :param error_type: Type of the error.
    :param field: Error field if allowed.
    :param message: Message for end-user.
    :param detail: Message for end-user.
    :return: ApiError container.
    """

    if error_type == ApiErrorType.AUTH_REQUIRED:
        return ApiError(
            status_code=401, code=1, type="AuthError",
            message=message if message else "Авторизуйтесь для продолжения!",
            detail=detail if detail else "Для выполнения данного метода, вы должны быть авторизованы!")

    if error_type == ApiErrorType.AUTH_DISSALOWED:
        return ApiError(
            status_code=400, code=2, type="AuthError",
            message=message if message else "Выйдите для продолжения!",
            detail=detail if detail else "Для выполнения данного метода, вы должны быть не авторизованы!")

    if error_type == ApiErrorType.AUTH_FAILED:
        return ApiError(
            status_code=400, code=3, type="AuthError",
            message=message if message else "Не верные данные для входа!",
            detail=detail if detail else "Данные которые вы предоставили не верны!")

    if error_type == ApiErrorType.AUTH_ALREADY_EXISTS:
        return ApiError(
            status_code=400, code=4, type="AuthError",
            message=message if message else "Данный аккаунт уже существует",
            detail=detail if detail else "Данные которые вы предоставили уже заняты другим пользователем!")

    if error_type == ApiErrorType.AUTH_PASSWORD_CONFIRMATION_MISMATCH:
        return ApiError(
            status_code=400, code=5, type="PaymentError",
            message=message if message else "Платёж успешно завершён!",
            detail=detail if detail else "Тестовый режим оплаты!")

    if error_type == ApiErrorType.FIELD_REQUIRED:
        return ApiError(
            status_code=400, code=6, type="ApiError",
            message=message if message else "Незаполненное поле!",
            detail=detail if detail else f"Заполните поле `{field}`!")

    if error_type == ApiErrorType.FIELD_INVALID:
        return ApiError(
            status_code=400, code=7, type="ApiError",
            message=message if message else "Некорректное поле!",
            detail=detail if detail else f"Поле `{field}` имеет некорректный формат!")

    if error_type == ApiErrorType.FIELD_TOO_LONG:
        return ApiError(
            status_code=400, code=8, type="ApiError",
            message=message if message else "Слишком длинное поле!",
            detail=detail if detail else f"Поле `{field}` слишком длинное!")

    if error_type == ApiErrorType.FIELD_TOO_SHORT:
        return ApiError(
            status_code=400, code=9, type="ApiError",
            message=message if message else "Слишком короткое поле!",
            detail=detail if detail else f"Поле `{field}` слишком короткое!")

    if error_type == ApiErrorType.PAYMENT_ERROR:
        return ApiError(
            status_code=400, code=10, type="PaymentError",
            message=message if message else "Платёж успешно завершён!",
            detail=detail if detail else "Тестовый режим оплаты!")

    return ApiError(
        status_code=500, code=0, type="InternalServerError",
        message="Неизвестная ошибка!",
        detail="Данная ошибка не зависит от вас! Пожалуйста напишите в поддержку!")
