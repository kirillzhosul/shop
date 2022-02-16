function handleError(data, status){
    if (!("error" in data)) return;

    if ("auth_required" in data && "redirect_to" in data){
        window.location = data["redirect_to"];
    }
}

function requestApi(method, params, handler){
    $.get("/api/" + method + "?" + params, function(data, status){
        if ("error" in data) return handleError(data, status);
        return handler(data, status)
    }).fail(function(xhr, status, error){
        return handleError(xhr.responseJSON, status);
    });
}