/*
Given an array of numbers (a list in groovy), determine whether the sum of all of the numbers is odd or even.

Give your answer in string format as 'odd' or 'even'.

If the input array is empty consider it as: [0] (array with a zero).
*/

const oddOrEven = arr => {
  if (arr == null || arr == undefined || arr.length == 0) return "even";
  let sum = 0;
  arr.map((e) => sum += e);
  return (sum % 2 == 0) ? "even" : "odd";
}


console.log(oddOrEven());


// Could use reduce
// function oddOrEven(arr) {
//   return arr.reduce((a,b)=>a+b,0) % 2 ? 'odd' : 'even';
// }