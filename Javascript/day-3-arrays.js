'use strict';

function getSecondLargest(nums) {
  let highestNum;
  let temp = [];
  let secondHighestNum;
  var curItem = 0; 
  let lastItem = 0;
  console.log("The array thats passed was: " + nums);

  nums.sort(function(a, b){return a-b});
  console.log("sorted array is: " + nums);

  nums.forEach(function(item, index, arr) {
    lastItem = curItem;
    curItem = item;
    
    if (curItem !== lastItem) {
      temp.push(curItem);
    }

  });

  temp.sort(function(a, b){return a-b});
  console.log("temp array is: " + temp);

  secondHighestNum = temp[temp.length - 2];

  console.log("Second highest number is: " + secondHighestNum);

  return secondHighestNum
}


var testArr = [1,2,7,4,5,6,8,9,10];

console.log(getSecondLargest(testArr));