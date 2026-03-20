/*--------------------------------
Problem 15: Swap Two Numbers Without Third Variable

Write a program that takes two numbers as input, swaps them without using any third variable (use
arithmetic operations), and displays values before and after swapping.
--------------------------------*/

let num1 = 35;
let num2 = 18;

console.log(`Before Swapping:`);
console.log(`Number 1: ${num1}, Number 2: ${num2}`);

num1 = num2 + num1;
num2 = num1 - num2;
num1 = num1 - num2;

console.log(`After Swapping:`);
console.log(`Number 1: ${num1}, Number 2: ${num2}`);

/* OUTPUT:
Before Swapping:
Number 1: 35, Number 2: 18
After Swapping:
Number 1: 18, Number 2: 35
*/
