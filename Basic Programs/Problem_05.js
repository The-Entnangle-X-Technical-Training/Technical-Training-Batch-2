/*--------------------------------
Problem 5: Swap Two Numbers Using Third Variable

Write a program that takes two numbers as input, swaps them using a third temporary variable, and
displays values before and after swapping.
--------------------------------*/

let num1 = 10;
let num2 = 20;

console.log("Before!");
console.log(`Number 1: ${num1}, Number 2: ${num2}`);

let swap = num1;
num1 = num2;
num2 = swap;

console.log("After!");
console.log(`Number 1: ${num1}, Number 2: ${num2}`);

/* OUTPUT:
Before!
Number 1: 10, Number 2: 20
After!
Number 1: 20, Number 2: 10
*/
