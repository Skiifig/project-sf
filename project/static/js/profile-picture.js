function autoclick() {
    document.getElementById('inputF').click()
}

function loadImg(event) {
    var icon = document.getElementById('icon-reg');
    const img = document.createElement("img")
    image_submitted = event.target.files[0]
    icon.replaceWith(img)
    img.src = (URL.createObjectURL(image_submitted))
    img.width = 100
    img.classList.add('rounded-circle')
}