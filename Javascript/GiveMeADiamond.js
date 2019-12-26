/*
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
*/

const diamond = n => {
  if (n % 2 == 0 || n == null || n == '' || n == undefined || n < 0) return null;

  let dia = "";
  let count = 1;
  const stop = Math.ceil(n / 2);

  const addStarOrSpace = (n, ch) => {
    let out = "";
    for (let i = 0; i < n; i++) out += ch;
    return out;
  };

  for (let j = 0; j < stop; j++) {
    dia += addStarOrSpace((Math.floor(n / 2) - j), " ");
    dia += addStarOrSpace(count, "*");
    dia += '\n';

    count += 2;
  }

  let reverseCount = 1;
  count -= 4;
  for (let k = stop; k > 1; k--) {
    dia += addStarOrSpace(reverseCount, " ");
    dia += addStarOrSpace(count, "*");
    dia += '\n';

    count -= 2;
    reverseCount += 1;
  }

  return dia;
}




console.log(diamond(5));