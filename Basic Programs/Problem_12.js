/*--------------------------------
Problem 12: Area of Triangle

Write a program that calculates the area of a triangle using the formula: Area = (base × height) / 2
--------------------------------*/

const calcAreaOfTriangle = (base, height) => {
  return (base * height) / 2;
};

const area = calcAreaOfTriangle(12, 32);

console.log(`Area of a triangle is: ${area}`);

/* OUTPUT:
Area of a triangle is: 192
*/
