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