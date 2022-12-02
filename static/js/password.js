function updateField() {
    passwordField = document.getElementById('password-field');
    if (passwordField.type == 'password') {
        passwordField.type = 'text'
    } else {
        passwordField.type = 'password'
    }
}