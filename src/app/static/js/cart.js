function addToCart(item_id){
    $.get("/api/cart/add?item_id=" + item_id.toString(), function(data, status){
        if ("error" in data){
            return; // TODO ERROR.
        }

        cart_item_id = data.cart_item_id;

        return;
    });
}

function removeFromCart(cart_item_id){
    $.get("/api/cart/remove?cart_item_id=" + cart_item_id.toString(), function(data, status){
        if ("error" in data){
            return; // TODO ERROR.
        }

        document.getElementById("cart-item-" + cart_item_id.toString()).remove();

        // TODO AJAX.
        window.location.reload();
        return;
    });
}

function orderCart(){
    $.get("/api/cart/order", function(data, status){
        if ("error" in data){
            return; // TODO ERROR.
        }

        // TODO AJAX(?????).
        window.location.reload();
        return;
    });
}