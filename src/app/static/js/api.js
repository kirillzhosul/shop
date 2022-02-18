function handleError(data, status){
    if (!("error" in data)) return;

    if ("redirect_to" in data){
        window.location = data["redirect_to"];
    }

    document.getElementById("api-error-message").innerText = data["error"];
}

function requestApi(method, params, handler){
    $.get("/api/" + method + "?" + params, function(data, status){
        if ("error" in data) return handleError(data, status);
        return handler(data, status)
    }).fail(function(xhr, status, error){
        return handleError(xhr.responseJSON, status);
    });
}