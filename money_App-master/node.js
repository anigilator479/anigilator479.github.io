
// Сума заробітку
function suma(){
    let num1,num2,result;
    num1 = document.getElementById("n1").value;
    num1 = parseInt(num1);
    num2 = document.getElementById("n2").value;
    num2 = parseInt(num2);
    result = num1 + num2;
    document.getElementById("sum").innerHTML = result;
    num4 = document.getElementById("enter_costsum").value;
    num4 = parseInt(num4);
    num5 = document.getElementById("inputt2").value;
    num5 = parseInt(num5);
    num6 = document.getElementById("inputt4").value;
    num6 = parseInt(num6);
    result2 = num4 + num5 + num6;
    document.getElementById("rizn").innerHTML = result2;
    result3=result-result2;
    document.getElementById("vmeste").innerHTML = result3;
};
// Появление форми
// target.addEventListener('click', viewDiv());
function viewDiv(){
document.getElementById('form_enter-costs').style.display = 'flex';
};
// добавление витрат
function btn() {
    let val = document.getElementById('enter_costname').value;
    document.getElementById('maincost').innerHTML=val;
    let pupa1 = document.getElementById("enter_costsum").value;
    document.getElementById('forCloseIcon').innerHTML=pupa1;
    let pupa2 = document.getElementById("input1").value;
    document.getElementById('maincostt').innerHTML=pupa2;
    let pupa3 = document.getElementById("inputt2").value;
    document.getElementById('forCloseIconn').innerHTML=pupa3;
    let pupa4 = document.getElementById("input3").value;
    document.getElementById('maincosttt').innerHTML=pupa4;
    let pupa5 = document.getElementById("inputt4").value;
    document.getElementById('forCloseIconnn').innerHTML=pupa5;
};
// Добавление инпутов 
let x = 0;
function addInput() {
let profile = document.getElementById('profile');
  let secondDiv = document.createElement('input');
  secondDiv.type = 'text';
  secondDiv.placeholder = 'Сума';
  let div = document.createElement('input');
  div.type = 'text';
  div.placeholder = 'Стаття витрат';
  div.id = 'input' + ++x;
  secondDiv.id = 'inputt' + ++x;
  profile.append(div);
  profile.append(secondDiv);
};

// кнопка для удаления  инпутов дороблю потом
// function delInput() {
//   let div = document.getElementById('input' + x);
//   div.remove();
//   --x;
// };


