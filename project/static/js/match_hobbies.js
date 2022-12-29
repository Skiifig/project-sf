function updateHobbies() {
    var input = document.getElementById('inputHobbies')
    var hobbies = input.value.split(',')
    for (i in hobbies) {
        var icon = document.getElementById(`icon-${i}`)
        var text = document.getElementById(`text-${i}`)
        switch (hobbies[i]) {
            case 'Musique':
                text.innerHTML = 'Aime la musique'
                icon.classList.add('fa-music')
                break;
            case 'Lecture':
                text.innerHTML = 'Aime la lecture'
                icon.classList.add('fa-book')
                break;
            case 'Jeux Vidéo':
                text.innerHTML = 'Aime les jeux-vidéo'
                icon.classList.add('fa-gamepad')
                break;
            case 'Cuisine':
                text.innerHTML = 'Aime la cuisine'
                icon.classList.add('fa-kitchen-set')
                break;
            case 'Cinéma':
                text.innerHTML = 'Aime le cinéma'
                icon.classList.add('fa-film')
                break;
        }
    }
}