
// ----------------- ÉNONCÉ -----------------

// Créer un algorithme qui sert à convertir des degrés Celsius
// en degrés Fahrenheit.
// Le résultat doit être de type nombre.
// Si on donne un autre type qu'un nombre en argument, vous
// devez retourner "Données en entrée non correctes."
// Bonne Chance !

const res = document.getElementById('response');
const form = document.getElementById('form');

const element_result = document.getElementById('element_result');
let sentence = '';
function transformCelsiusToFahrenheit(degCel){
    return (degCel * (9/5) + 32);
}
form.onkeydown = function(e){
    if(e.keyCode == 13){
        e.preventDefault();
        getSentenceResult()
    }
 };
function getSentenceResult(){
    const value = +res.value;
 
    if(isNaN(value)){
        return element_result.innerHTML = 'Données en entrée non correctes.';
    }
       const val = transformCelsiusToFahrenheit(value);
       return  element_result.innerHTML =  value + ' degrés Celsius donne ' + parseInt(val) + ' Fahrenheit ';
}
