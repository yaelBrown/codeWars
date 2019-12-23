/*
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
*/

const removeChar = (str) => str.substring(1).substring(0,str.length - 2);

console.log(removeChar("person"));








// could of used str.slice method !

// const removeChar = (str) => str.substring(1).substring(0, -1);
// const removeChar = (str) => str.slice(1,-1);