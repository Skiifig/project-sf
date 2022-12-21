function handleClick(inputName, reponse) {
    var inputO = document.getElementById('orientation')
    var inputS = document.getElementById('sexe')
    var inputH = document.getElementById(inputName);
    inputH.value = reponse
    if (inputO.value && inputS.value) {
        if (inputO.value == inputS.value) {
            inputO.value = "homosexuel"
        } else {
            inputO.value = "hétérosexuel"
        }
    }
}

function handleCheck(hobbie) {
    input = document.getElementById("hobbies")
    if (!input.value) {
        input.value = hobbie
    } else if (input.value) {
        hobbies_submitted = input.value.split(' ')
        if (hobbie in hobbies_submitted) {
            for (const i in hobbies_submitted) {
                if (hobbie == hobbies_submitted) {}
            }
        } else {
            input.value = input.value + ' ' + hobbie
        }
    }
}