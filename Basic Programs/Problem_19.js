/*--------------------------------
Problem 19: Simple Interest with Total Amount

Write a program that takes principal amount, rate of interest, and time period as input, calculates simple
interest and total amount (Principal + SI), then displays both values.
--------------------------------*/

const p = 5000;
const r = 2;
const t = 3;

const si = (p * r * t) / 100;

const amt = p + si;

console.log(`The Simple Interest is: ${si}`);
console.log(`The amount will be: ${amt}`);

/* OUTPUT:
The Simple Interest is: 300
The amount will be: 5300
*/
