// function fizzbuzz(n) {
//     console.log("n = " + n);
//     for (i = 1; i <= n; i++){
//         if(i % 3 == 0) {
//             console.log("fizz");
//         } else if (i % 5 == 0) {
//             console.log("buzz");
//         } else if (i % 15 == 0) {
//             console.log("fizzbuzz");
//         } else {
//             console.log(i);
//         };
//     };
// };
//
// fizzbuzz(100);


// ==================

const fizzBuzz = num => {
    if (num % 15 === 0) return n + ' fizzbuzz';
    else if (num % 5 === 0 ) return n + ' fizz';
    else if (num % 3 === 0 ) return n + ' buzz';
    else return num;
};

let n = 15;

while (n != 0) {
    console.log(fizzBuzz(n));
    n--;
}

// ==================

for (let i=0; i<100; ) console.log((++i % 3 ? '' : 'fizz' ) + ( i % 5 ? '' : 'buzz' ) || i );