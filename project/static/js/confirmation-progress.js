var field_filled = 0;

function updateProgress(event) {
    var bar = document.getElementsByClassName('progress-bar')[0];
    field_filled += 1
    value_bar = 50 + field_filled / 3 * 50
    bar.style.width = `${Math.round(value_bar)}%`
    console.log(value_bar)
}