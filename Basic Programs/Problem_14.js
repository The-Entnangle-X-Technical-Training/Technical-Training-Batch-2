/*--------------------------------
Problem 14: Area and Perimeter of Rectangle

Write a program that takes length and width of a rectangle as input and calculates both its area and
perimeter, then displays both results.
--------------------------------*/

const length = 18;
const width = 9;

const areaOfRectangle = length * width;
const perimeterOfRectangle = 2 * areaOfRectangle;

console.log(`Area of Rectangle is: ${areaOfRectangle}`);
console.log(`Perimeter of Rectangle is: ${perimeterOfRectangle}`);

/* OUTPUT:
Area of Rectangle is: 162
Perimeter of Rectangle is: 324
*/
