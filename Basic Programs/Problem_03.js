/*--------------------------------
Problem 3: Simple Calculator

Write a program that takes two numbers from the user and performs addition, subtraction, multiplication,
division, and modulus on them, displaying all five results
--------------------------------*/

const num1 = 46;
const num2 = 37;

const sum = num1 + num2;
const sub = num1 - num2;
const mul = num1 * num2;
const div = num1 / num2;
const mod = num1 % num2;

console.log(`The sum of ${num1} + ${num2}: ${sum}`);
console.log(`The subtraction of ${num1} - ${num2}: ${sub}`);
console.log(`The multiplication of ${num1} * ${num2}: ${mul}`);
console.log(`The division of ${num1} / ${num2}: ${div}`);
console.log(`The modulus of ${num1} % ${num2}: ${mod}`);

/* OUTPUT:
The sum of 46 + 37: 83
The subtraction of 46 - 37: 9
The multiplication of 46 * 37: 1702
The division of 46 / 37: 1.2432432432432432
The modulus of 46 % 37: 9
*/
