/// @description API Library for http://shop.kirillzhosul.site/
/// @author Kirill Zhosul.
/// @license (c) 2022 Kirill Zhosul.

API_BASE_URL = "/api/";
API_ERROR_CONTAINER = "error";
API_ERROR_ELEMENT_ID = "api-error"

function handleApiErrorResponse(data, status){
    /// @description Wrapper for error API responses.
    if (data === undefined) return;
    if (!(API_ERROR_CONTAINER in data)) return;

    var error = data[API_ERROR_CONTAINER];
    var code = error["code"];
    var type = error["type"];
    var message = error["message"];
    var detail = error["detail"];

    var error_element = document.getElementById(API_ERROR_ELEMENT_ID);

    error_element.innerHTML = "[" + code + "] " + type + "<br>" + message + "<br>" + detail;
}

function requestApi(method, params, handler){
    /// @description Wrapper for the API requests.
    $.get(API_BASE_URL + method + "?" + params, function(data, status){
        if (API_ERROR_CONTAINER in data) handleApiErrorResponse(data, status);
        return handler(data, status)
    }).fail(function(xhr, status, error){
        return handleApiErrorResponse(xhr.responseJSON, status);
    });
}