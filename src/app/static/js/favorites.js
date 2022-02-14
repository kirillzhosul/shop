function addToFavorites(item_id){
    $.get("/api/favorites/add?item_id=" + item_id.toString(), function(data, status){
        if ("error" in data){
            return; // TODO ERROR.
        }
    });
}

function removeFromFavorites(favorite_item_id){
    $.get("/api/favorites/remove?favorite_item_id=" + favorite_item_id.toString(), function(data, status){
        if ("error" in data){
            return; // TODO ERROR.
        }

        document.getElementById("favorite-item-" + favorite_item_id.toString()).remove();

        // TODO AJAX.
        window.location.reload();
        return;
    });
}