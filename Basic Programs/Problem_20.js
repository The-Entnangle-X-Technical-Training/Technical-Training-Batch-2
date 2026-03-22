/*--------------------------------
Problem 20: Profit or Loss Calculator

Write a program that takes cost price and selling price as input, then determines and displays whether it's
profit or loss and calculates the amount.
--------------------------------*/

const cp = 650;
const sp = 550;

console.log(`Cost price is: ${cp}, Selling price is: ${sp}`);

if (sp > cp) {
  const profit = sp - cp;
  console.log(`It's Profit hurray! Amount is: ${profit}`);
} else if (cp > sp) {
  const loss = cp - sp;
  console.log(`Ohh it's Loss! Amount is: ${loss}`);
}

/* OUTPUT:
if selling price is greater than cost price then it is profit:
Cost price is: 500, Selling price is: 650
It's Profit hurray! Amount is: 150

if selling price is smaller than cost price then it is loss:
Cost price is: 650, Selling price is: 550
Ohh it's Loss! Amount is: 100
*/
