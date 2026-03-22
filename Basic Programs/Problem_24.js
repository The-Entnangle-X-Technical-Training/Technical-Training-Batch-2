/*--------------------------------
Problem 24: BMI Calculator

Write a program that calculates Body Mass Index using: BMI = weight(kg) / (height(m))²
--------------------------------*/

const weight = 68;
const height = 1.64;

const BMI = weight / height ** 2;

console.log(
  `Body Mass Index (BMI) for Weight ${weight}kg, Height ${height}m is: ${BMI}`,
);

/* OUTPUT:
Body Mass Index (BMI) for Weight 68kg, Height 1.64m is: 25.282569898869724
*/
