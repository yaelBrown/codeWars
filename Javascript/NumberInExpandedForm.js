/*
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(12); // Should return '10 + 2'
expandedForm(42); // Should return '40 + 2'
expandedForm(70304); // Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
*/

// const expandedForm = (n) => {
//   let out = "";
//   let temp = n.toString().split("");
//   let count = temp.length;

//   const addZeros = (z) => {
//     let out = "";
//     for (let i = 0; i < z; i++) out += "0";
//     return out;
//   }


//   temp.map((e) => {
//     if (e != 0) {
//       if (count == 1) {
//         out += e;
//         count--;
//       } else {
//         out += e;
//         out += addZeros(count - 1);
//         out += " + "
//         count--;
//       }
//     } else {
//       count--;
//     }
//   })

//   return out;
// }


// const expandedForm = (n) => {
//   let out = "";
//   let temp = n.toString().split("");
//   let count = temp.length;

//   const addZeros = (z) => {
//     let out = "";
//     for (let i = 0; i < z; i++) out += "0";
//     return out;
//   }


//   temp.map((e,i) => {
//     if (e != 0) {
//       if (count == 1) {
//         out += e;
//         count--;
//       } else if (count == temp.length) {
//         out += e;
//         out += addZeros(count - 1);
//         count--;
//       } else if (count > 1) {
//         out += " + "
//         out += e;
//         out += addZeros(count - 1);
//         count--;
//       } else {
//         out += e;
//         out += addZeros(count - 1);
//         count--;
//       }
//     } else {
//       count--;
//     }
//   })
//   return out;
// }

// const expandedForm = (n) => {
//   let out = "";
//   let temp = n.toString().split("");


//   const addZeros = (z) => {
//     let out = "";
//     for (let i = 0; i < z; i++) out += "0";
//     return out;
//   }

//   let count = temp.length;
//   for (let i = 0; i < temp.length; i++) {
//     if (temp[i] > 0 && count != 1) {
//       out += temp[i];
//       out += addZeros(count - 1);
//       count--;
//     } else if (temp[i] > 0 && count == 1) {
//       out += temp[i];
//     } else if(temp[i] > 0 && count > 1) {
//       out += " + ";
//       out += temp[i];
//       out += addZeros(count - 1);
//       count--;
//     } else {
//       count--;
//     }
//   }

//   return out;
// }

console.log(expandedForm(70000));
console.log(expandedForm(70304));


console.log(expandedForm(70000));
console.log(expandedForm(70304));

console.log(expandedForm(70304));


// I will come back to this