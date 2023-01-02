function autoclick() {
    document.getElementById('inputF').click()
}

function loadImg(event) {
    var icon = document.getElementById('icon-reg');
    const img = document.createElement("img"); // Création de la nouvelle balise image
    image_submitted = event.target.files[0]; // Définition de l'image
    icon.replaceWith(img); // Remplacement de l'icone par l'image
    img.src = (URL.createObjectURL(image_submitted)); // Récupération de l'image
    img.width = 100; // Définition de la taille de l'image
    img.classList.add('rounded-circle'); // Arrondissement de l'image
}