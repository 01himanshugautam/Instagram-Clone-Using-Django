console.log("Validate");
var _email, _name, _password, _username;

function validate() {
    console.log("Click on Validate");
    _email = document.getElementById('email');
    _name = document.getElementById('name');
    _password = document.getElementById('password');
    _username = document.getElementById('username');
    let mail = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
    if (_email.value.match(mail)) {
        _email.classList.add("error");
    }
    console.log(_email.value, _name.value, _password.value, _username.value);
}



function email() {
    _email = document.getElementById('email');
    // let mail = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
    // if (!_email.value.match(mail)) {
    //     _email.classList.add(" error");
    // }
    console.log(_email.value);
}