function calc() {
    year = document.getElementById("year-select").value;
    month = document.getElementById("month-select").value;
    day = document.getElementById("day-select").value;
    field = document.getElementById("age-field");
    var birthDay = new Date(year, month, day);
    diff = Date.now() - birthDay.getTime();
    var age_calc = new Date(diff);
    age = Math.abs(age_calc.getUTCFullYear() - 1970);   
    if (!year || !month || !day) {
        res = undefined
    } else if (age < 15) {
        res = 'Vous devez avoir plus de 15 ans pour vous inscrire'
        field.classList.replace("text-primary", "text-danger")
        document.querySelector('#submit').disabled = true;
    } else {
        res = 'Vous avez ' + `${age}` + ' ans'
        field.classList.replace("text-danger", "text-primary")
        document.querySelector('#submit').disabled = false;
    }
    if (res) {
        field.type = 'text';
        field.value = res;
    }
}