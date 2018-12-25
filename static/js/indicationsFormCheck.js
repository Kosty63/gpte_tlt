
    var monthNames = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь",
    "Октябрь", "Ноябрь", "Декабрь"];

    var date = new Date();

    var inputPeriud = document.getElementById('periud');

    if (date.getDate() < 20){

        inputPeriud.value = monthNames[date.getMonth()];

    }else {
        if (date.getMonth() >= 11){
            inputPeriud.value = monthNames[0]
        }else {
        inputPeriud.value = monthNames[date.getMonth() + 1]
        }
    }

    inputPeriud.setAttribute('readonly', 'readonly');
