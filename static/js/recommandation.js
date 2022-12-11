function recommend(event) {
    const searchWrapper = document.querySelector("#question-container")
    const inputBox = document.querySelector("#input-city");
    const suggBox = document.querySelector(".autocom-box");
    let userData = event.target.value;
    let emptyArray = [];
    if (userData) {
        emptyArray = suggestions.filter((data) => {
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data) => {
            return data = '<li>' + data + '</li>';
        });
        searchWrapper.classList.add("active");
        showRecommandation(emptyArray, inputBox ,suggBox);
        let allList = document.getElementsByTagName('li');
        for (let i = 0; i < allList.length; i++) {
            allList[i].setAttribute("onclick", "select(this)")
        }
    } else {
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