/*
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
*/

// const jadenCase = (str) => {
//   if (!str) str = this;
//   word = str.split(" ");
//   out = "";
//   word.map((e,i) => {
//     e = e.substring(0,1).toUpperCase() + e.substring(1,e.length);

//     if (i == (word.length - 1)) {
//       out += e;
//     } else {
//       out += e + " ";
//     }

//   });
//   return out;
// }

String.prototype.toJadenCase = function () {
  word = this.split(" ");
  out = "";
  word.map((e,i) => {
    e = e.substring(0,1).toUpperCase() + e.substring(1,e.length);

    if (i == (word.length - 1)) {
      out += e;
    } else {
      out += e + " ";
    }

  });
  return out;
};

let aa = "This is a String";
console.log(aa.toJadenCase());

// console.log(jadenCase(aa))
// console.log(aa);






// Could also have been completed with regular expression
//    https://regex101.com/