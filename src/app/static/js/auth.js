function authLogin(email, password){
    requestApi("auth/login", "email=" + email.toString() + "&password=" + password.toString(), function(data, status){
        if ("redirect_to" in data){
            window.location = data["redirect_to"];
        }
    });
}

function authRegister(name, phone, email, password, passwordConfirmation){
    var params = "";
    params += "name=" + name.toString();
    params += "&phone=" + phone.toString();
    params += "&email=" + email.toString();
    params += "&password=" + password.toString();
    params += "&password_confirmation=" + passwordConfirmation.toString();

    requestApi("auth/register", params, function(data, status){
        if ("redirect_to" in data){
            window.location = data["redirect_to"];
        }
    });
}

function authLogout(){
    requestApi("auth/logout", "", function(data, status){
        if ("redirect_to" in data){
            window.location = data["redirect_to"];
        }
    });
}