var countOne = 0;
var clickCounter = document.querySelector("#clickCounter");

function clickOne(element){
    countOne++;
    console.log(countOne);
    clickCounter.innerText=(countOne);
}

function resetOne(element){

}