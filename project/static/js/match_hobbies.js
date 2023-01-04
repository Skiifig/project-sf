function updateHobbies() {
    var len_match = document.getElementById('lenMatch').value; // On compte le nombre de match donnés par le serveur
    for (j = 0; j < len_match; j++) {
        var input = document.getElementsByName('inputHobbies')[j];
        var match_btn = document.getElementsByClassName('btn-modal')[j]; // Selection du bouton propre à la carte
        var hobbies = input.value.split(','); // Séparation des hobbies en 2
        for (i in hobbies) {
            var icon = document.getElementById(`icon-${i}-${j}`); // Selection de chaque icone
            var text = document.getElementById(`text-${i}-${j}`); // Selection chaque texte
            switch (hobbies[i]) {
                case 'Musique': // Dans le cas où l'utilisateur aime la musique
                    text.innerHTML = 'Aime la musique'; // Ajout du texte
                    icon.classList.add('fa-music'); // Ajout de l'icone
                    break;
                case 'Lecture': // // Dans le cas où l'utilisateur aime la lecture
                    text.innerHTML = 'Aime la lecture';
                    icon.classList.add('fa-book');
                    break;
                case 'Jeux vidéo':
                    text.innerHTML = 'Aime les jeux-vidéo';
                    icon.classList.add('fa-gamepad');
                    break;
                case 'Cuisine':
                    text.innerHTML = 'Aime la cuisine';
                    icon.classList.add('fa-kitchen-set');
                    break;
                case 'Cinéma':
                    text.innerHTML = 'Aime le cinéma';
                    icon.classList.add('fa-film');
                    break;
            }
            if (hobbies.length == 1) { // S'il n'y a qu'un seul centre d'intérêt
                match_btn.classList.add('mt-auto') // Ajout d'une classe qui descendra le bouton
            }
        }
    }
}