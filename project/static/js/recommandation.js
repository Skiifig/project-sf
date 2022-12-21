function recommend(event) {
    const searchWrapper = document.querySelector("#question-container")
    const inputBox = document.querySelector("#input-city");
    const suggBox = document.querySelector(".autocom-box");
    let userData = event.target.value;
    let emptyArray = [];
    if (userData) { // Si l'input n'est pas vide
        emptyArray = suggestions.filter((data) => {
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase()); // Rajouter les villes qui commencent par le début de l'input dans le tableau
        });
        emptyArray = emptyArray.map((data) => {
            return data = '<li>' + data + '</li>'; // Ajout de l'html pour chaque valeur du tableau
        });
        searchWrapper.classList.add("active");
        showRecommandation(emptyArray, inputBox ,suggBox);
        let allList = document.getElementsByTagName('li'); // Prendre tous les éléments ayant le tag 'li'
        for (let i = 0; i < allList.length; i++) { // Pour chaque élement
            allList[i].setAttribute("onclick", "select(this)") // Rajouter l'attribut onclick avec l'appel de la fonction select
        }
    } else { // Sinon cacher les recommandations
        searchWrapper.classList.remove("active")
    }
}

function select(element) {
    let selectUserData = element.textContent;
    const searchWrapper = document.querySelector("#question-container");
    const inputBox = document.querySelector("#input-city");
    inputBox.value = selectUserData;
    searchWrapper.classList.remove("active");
}

function showRecommandation(list, input, element) {
    let listData;
    if (!list.length) {
        userValue = input.value
        listData = '<li>' + userValue + '</li>';
    }
    else {
        listData = list.join('');
    }
    element.innerHTML = listData;
}