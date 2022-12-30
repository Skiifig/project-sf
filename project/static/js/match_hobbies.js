function updateHobbies() {
    var len_match = document.getElementById('lenMatch').value;
    for (j = 0; j < len_match; j++) {
        var input = document.getElementsByName('inputHobbies')[j];
        var match_btn = document.getElementsByClassName('btn-modal')[j];
        var hobbies = input.value.split(',');
        for (i in hobbies) {
            var icon = document.getElementById(`icon-${i}-${j}`);
            var text = document.getElementById(`text-${i}-${j}`);
            switch (hobbies[i]) {
                case 'Musique':
                    text.innerHTML = 'Aime la musique';
                    icon.classList.add('fa-music');
                    break;
                case 'Lecture':
                    text.innerHTML = 'Aime la lecture';
                    icon.classList.add('fa-book');
                    break;
                case 'Jeux Vidéo':
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
            if (hobbies.length == 1) {
                match_btn.classList.add('mt-auto')
            }
        }
    }
}