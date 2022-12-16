// Ce fichier sert à remplir automatiquement les selector
year = new Date().getFullYear() // Obtenir l'année actuelle
var monthNames = [ "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
"Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre" ];

function CreateDay(i) { // Fonction pour remplir selector des jours
    Day = document.getElementById("day-select"); // Selection du selector des jours
    Day.innerHTML = Day.innerHTML + `<option>${i}</option>` // Changement du contenu du selector selon la valeur de i
}

function CreateMonth(i) { // Fonction pour remplir selector des mois
    Month = document.getElementById("month-select"); // Selection du selector des mois
    Month.innerHTML = Month.innerHTML + `<option id='month'>${i}</option>` // Changement du contenu du selctor selon la valeur de i
}

function CreateYear() { // Fonction pour remplir selector des années
    Year = document.getElementById("year-select"); // Selection du selector des années
    Year.innerHTML = Year.innerHTML + `<option>${year}</option>` // Changement du contenu du selector selon year
    year = year - 1
}

function FillAllSelector() {
    for (let i = 0; i <= 31; i++) { // Boucle for avec i => 1-31
        CreateDay(i)
    }
    for (let i = 0; i <= 12; i++) { // Boucle for avec i => 1-12
        CreateMonth(i)
    }
    for (let i = 0; i <= 100; i++) { // Boucle for avec i => 1-100
        CreateYear()
    }
}