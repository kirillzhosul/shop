function addToCart(item_id){
    requestApi("cart/add", "item_id=" + item_id.toString(), function(data, status){});
}

function removeFromCart(cart_item_id){
    requestApi("cart/remove", "cart_item_id=" + cart_item_id.toString(), function(data, status){
        // document.getElementById("cart-item-" + cart_item_id.toString()).remove();
        window.location.reload();  // TODO AJAX.
    });
}

function orderCart(){
    requestApi("cart/order", "", function(data, status){
        window.location.reload(); // TODO AJAX.
    });
}

function clearCart(){
    requestApi("cart/clear", "", function(data, status){
        window.location.reload(); // TODO AJAX.
    });
}