/*--------------------------------
Problem 23: Electricity Bill Calculator

Write a program that calculates electricity bill based on units consumed and rate per unit, then displays
the total bill amount.
--------------------------------*/

const unitsConsumed = 200;
const unitRate = 6;
const fixedCharge = 100;

const eleCharged = unitsConsumed * unitRate;

const totalBillAmt = eleCharged + fixedCharge;

console.log(
  `Unit Consumed: ${unitsConsumed}, Rate per unit: ${unitRate}, Fixed charged: ${fixedCharge}`,
);
console.log(
  `Electricity charged: ${eleCharged}, Total bill amount: ${totalBillAmt}`,
);

/* OUTPUT:
Unit Consumed: 200, Rate per unit: 6, Fixed charged: 100
Electricity charged: 1200, Total bill amount: 1300
*/
