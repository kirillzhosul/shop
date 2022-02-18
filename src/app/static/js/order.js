function orderPay(order_id){
    requestApi("order/pay", "order_id=" + order_id.toString(), function(data, status){});
}
