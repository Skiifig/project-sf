function autoclick() {
    document.getElementById('inputF').click()
}

function loadImg(event) {
    var content = document.getElementById('input-container');
    image_submitted = event.target.files[0]
    content.innerHTML = `<img src="${URL.createObjectURL(image_submitted)}" class="rounded-circle" height=120 width=120 id="output" name="profile_pic" accept="image/png image/jpg">`;
}