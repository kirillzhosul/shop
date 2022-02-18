function authLogin(email, password){
    requestApi("auth/login", "email=" + email.toString() + "&password=" + password.toString(), function(data, status){
        if ("redirect_to" in data){
            window.location = data["redirect_to"];
        }
    });
}