var field_filled = 0;

function updateProgress(event) {
    var bar = document.getElementsByClassName('progress-bar')[0]; // Selection de la barre de progression
    field_filled += 1 // Incrémentation de la variable de 1
    value_bar = field_filled / 8 * 50 // Calcul de la nouvelle taille de la barre
    bar.style.width = `${Math.round(value_bar)}%` // Application de la nouvelle taille avec arondissement
    if (event.target.classList.contains('select')) {
        event.target.removeAttribute('onfocus')
    } else {
        event.target.removeAttribute('onchange') // Cette fonction ne se déclenche qu'une fois par élément
    }
}