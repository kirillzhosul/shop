function handleError(data, status){
    if (data === undefined) return;
    if (!("error" in data)) return;

    if ("redirect_to" in data){
        window.location = data["redirect_to"];
    }

    document.getElementById("api-error-message").innerText = data["error"];
}

function requestApi(method, params, handler, evenOnError=false){
    $.get("/api/" + method + "?" + params, function(data, status){
        if ("error" in data){
            handleError(data, status);
            if (!evenOnError) return;
        }
        return handler(data, status)
    }).fail(function(xhr, status, error){
        return handleError(xhr.responseJSON, status);
    });
}