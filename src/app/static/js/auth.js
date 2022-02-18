function authLogin(){
    requestApi("auth/login", "email=kirill_zhosul@vk.com&password=test", function(data, status){
        if ("redirect_to" in data){
            window.location = data["redirect_to"];
        }
    });
}