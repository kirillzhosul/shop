function addToFavorites(item_id){
    requestApi("favorites/add", "item_id=" + item_id.toString(), function(data, status){});
}

function removeFromFavorites(favorite_item_id){
    requestApi("favorites/remove", "favorite_item_id=" + favorite_item_id.toString(), function(data, status){
        // TODO AJAX.
        // document.getElementById("favorite-item-" + favorite_item_id.toString()).remove();
        window.location.reload();
    });
}