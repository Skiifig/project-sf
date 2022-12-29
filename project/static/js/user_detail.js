function handleClick(inputName, reponse) {
    var inputO = document.getElementById('orientation');
    var inputS = document.getElementById('sexe');
    var inputH = document.getElementById(inputName);
    inputH.value = reponse;
    updateProgress(event)
    if (inputO.value && inputS.value) { // Si les deux inputs sont remplis
        if (inputO.value == inputS.value) { // Si les deux inputs sont égaux
            inputO.value = "Homosexuel"
        } else {
            inputO.value = "Hétérosexuel"
        }
    }
}

function handleCheck() {
    var array = []
    var submitBtn = document.getElementById('validation');
    var checkboxes = document.querySelectorAll('input[type=checkbox]:checked'); // Création d'une variable contentant toutes les cases cochées
    var input = document.getElementById('hobbies');
    for (var i = 0; i < checkboxes.length; i++) { // Pour i dans le nombre de cases cochées
        array.push(checkboxes[i].value); // On ajoute dans le tableau la valeur de chaque case
    }
    input.value = array; // L'input prend la valeur du tableau
    if (array.length == 0 || array.length > 2) {
        submitBtn.disabled = true; // On désactive le bouton
    } else {
        submitBtn.disabled = false; // On active le bouton
    }
}