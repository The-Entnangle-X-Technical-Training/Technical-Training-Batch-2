/*--------------------------------
Problem 22: Total Cost Calculator with Tax

Write a program that calculates total cost of items: input price, quantity, and tax percentage, then calculate
and display subtotal, tax amount, and final total amount.
--------------------------------*/

const itemPrice = 115;
const qty = 1;
const taxPercent = 18;

const subTotal = itemPrice * qty;
const taxAmt = subTotal * (taxPercent / 100);
const finalAmt = subTotal + taxAmt;

console.log(`Item price was: ${itemPrice}`);
console.log(`Quantity: ${qty}`);
console.log(`Tax percent: ${taxPercent}`);

console.log(
  `Subtotal: ${subTotal}, Tax amount: ${taxAmt}, Final amount: ${finalAmt}`,
);

/* OUTPUT:
Item price was: 115
Quantity: 1
Tax percent: 18
Subtotal: 115, Tax amount: 20.7, Final amount: 135.7
*/
