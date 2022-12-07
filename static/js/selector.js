year = new Date().getFullYear()
var monthNames = [ "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
"Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre" ];

function CreateDay(i) {
    Day = document.getElementById("day-select");
    Day.innerHTML = Day.innerHTML + `<option>${i}</option>`
}

function CreateMonth(i) {
    Month = document.getElementById("month-select");
    Month.innerHTML = Month.innerHTML + `<option id='month'>${i}</option>`
}

function CreateYear() {
    Year = document.getElementById("year-select");
    Year.innerHTML = Year.innerHTML + `<option>${year}</option>`
    year = year - 1
}

function FillAllSelector() {
    for (let i = 0; i <= 31; i++) {
        CreateDay(i)
    }
    for (let i = 0; i <= 12; i++) {
        CreateMonth(i)
    }
    for (let i = 0; i <= 100; i++) {
        CreateYear()
    }
}