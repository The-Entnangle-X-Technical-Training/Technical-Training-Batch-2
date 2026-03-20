/*--------------------------------
Problem 6: Percentage Calculator

Write a program that takes marks in 3 subjects (out of 100 each) as input, calculates total marks out of
300 and percentage, then displays both
--------------------------------*/

const mathsMarks = 48;
const physicsMarks = 56;
const historyMarks = 52;

const marksSum = mathsMarks + physicsMarks + historyMarks;

const percentage = (marksSum / 300) * 100;

console.log(
  `Marks of Maths: ${mathsMarks}, Marks of Physics: ${physicsMarks}, Marks of History: ${historyMarks}`,
);
console.log(`There sum is: ${marksSum} & the percentage is: ${percentage}`);

/* OUTPUT:
Marks of Maths: 48, Marks of Physics: 56, Marks of History: 52
There sum is: 156 & the percentage is: 52
*/
