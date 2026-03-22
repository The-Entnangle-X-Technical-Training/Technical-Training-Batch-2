/*--------------------------------
Problem 18: Average of Marks in 5 Subjects

Write a program that takes marks obtained in 5 subjects as input, calculates the total marks and average
marks, and displays both.
--------------------------------*/

const maths = 37;
const physics = 43;
const english = 64;
const hindi = 51;
const chemistry = 43;

const average = maths + physics + english + hindi + chemistry / 5;
console.log(`Average is: ${average}`);

/* OUTPUT:
Average is: 203.6
*/
