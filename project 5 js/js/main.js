// 1  
    // let Arr1=[1, 5, "4", "hello"],
    //     Arr2=[true,2, {}, ["a"], 222];
    //     console.log(Arr1[1]);
    //     console.log(Arr2[1]);
    //     console.log(Arr1[1]+Arr2[1]);
// 2
// let Arr1=[1, 5, "4", "hello"];
//     Arr1.push(22);
//     console.log(Arr1);
// 3
// let Arr2=[true,2, {}, ["a"], 222],
//     Arr1;
// for (Arr1 of Arr2 ){
//   console.log(typeof Arr1);
// }
// 4
// let result = 0;
// const matrix =  [
//     [10,11,12],
//     [13,14,15],
//     [16,17,18],
// ];
// for (let i = 0; i < matrix.length; i += 1) {
//     console.log (matrix[i]);
  
//     for (let j = 0; j < matrix[i].length; j += 1) {
//       console.log(matrix[i][j]);
//       result += matrix[i][j];
//     }
//   }
// 5
// const message = 'Welcome to Ukraine!';
// a=message.split([]);
// console.log(a);
// console.log(message.indexOf('l'));
// console.log(a.join(''));
// 6
// stack=[],
// steel=[2,3,4],
// cook=[5,6,7,8];

// for(let i=0;i<steel.length;i++){
//     stack.unshift(steel[i]);
// }
// for(let j=0;j<cook.length;j++){
//     stack.push(cook[j]);
// }
// console.log(stack);
//7
// let stack=[2,3,4,5,6,7,8],
// lastNumbers=[];
// lastNumbers = stack.splice(4,3);
// console.log(lastNumbers);
//8
// let animals = ["pig","dog","cat","parrot","chicken"],
//     pets = [];
// pets = animals.splice(2, 3);
// console.log(animals);
// console.log(pets);
9
let pets = ["cat","parrot","chicken"];
pets.splice(2,1,"shark","elephant");
console.log(pets);
