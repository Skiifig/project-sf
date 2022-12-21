function calc() {
    inputH = document.getElementById("age");
    year = document.getElementById("year-select").value;
    month = document.getElementById("month-select").value;
    day = document.getElementById("day-select").value;
    field = document.getElementById("age-field");
    var birthDay = new Date(year, month, day); // Création d'une nouvelle date à partir des données de l'utilisateur
    diff = Date.now() - birthDay.getTime(); // Calcul de la différence
    var age_calc = new Date(diff); // Création d'une nouvelle date à partir de la différence
    age = Math.abs(age_calc.getUTCFullYear() - 1970);
    if (!year || !month || !day) { // Si une des valeurs n'est pas définie
        res = undefined // Aucune réponse
    } else if (age < 15) { // Si l'utilisateur a moins de 15 ans
        res = 'Vous devez avoir plus de 15 ans pour vous inscrire'
        field.classList.replace("text-primary", "text-danger") // Changement de couleur du texte
        document.querySelector('#submit').disabled = true; // Désactivation du boutton de validation
    } else {
        res = 'Vous avez ' + `${age}` + ' ans'
        field.classList.replace("text-danger", "text-primary")
        document.querySelector('#submit').disabled = false; // Activer le bouton de validation
        inputH.value =  age
    }
    if (res) { // Si la réponse est définie
        field.type = 'text'; // Montrer l'input
        field.value = res;
    }
}