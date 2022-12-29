var field_filled = 0;

function updateProgress(event) {
    var bar = document.getElementsByClassName('progress-bar')[0];
    if (event.target.value) {field_filled += 1} else {field_filled -= 1}
    value_bar = field_filled / 8 * 50
    bar.style.width = `${Math.round(value_bar)}%` 
}