function updateField() {
    passwordField = document.getElementById('password-field'); // Sélection du champ de mot de passe
    if (passwordField.type == 'password') { // Si l'input est de type mot de passe
        passwordField.type = 'text' // Changer en text
    } else {
        passwordField.type = 'password' // Sinon changer en mot de passe
    }
}