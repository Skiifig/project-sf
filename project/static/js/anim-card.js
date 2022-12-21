async function cardSynchro() {
    cards = document.getElementsByClassName('bg-dark') // On sélectionne les cartes à partir du classe qu'elles sont les seules à avoir
    for (const i of cards) { // Pour i dans le nombre de cartes (3)
        i.classList.add('fade-in') // Ajout de la classe qui fait l'animation
        await new Promise(r => setTimeout(r, 2000)); // Attendre 2 secondes
        i.style.opacity = 1 // Révéler la carte
    }
}