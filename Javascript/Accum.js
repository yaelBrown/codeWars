/*
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
*/

const accum = s => {
  let strArr = s.toLowerCase().split("");
  let addLtrs = "";

  strArr.map((e,i) => {
    for (let j = 0; j <= i; j++) addLtrs += e;
    addLtrs = addLtrs.charAt(0).toUpperCase() + addLtrs.substring(1);
    strArr[i] = addLtrs;
    addLtrs = "";
  })

  return strArr.join("-");
}

console.log(accum("RqaEzty"));




// .repeat method repeats adding characters to string. So you don't have to use L16