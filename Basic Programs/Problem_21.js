/*--------------------------------
Problem 21: Discount Price Calculator\

Write a program that calculates the final price after applying a discount percentage on the original price.
--------------------------------*/

const originalPrice = 300;
const discount = 10;

const discountedAmt = originalPrice * (discount / 100);
const finalPrice = originalPrice - discountedAmt;

console.log(
  `Original Price was: ${originalPrice}, Discount applied: ${discount}%`,
);
console.log(`Final Price is: ${finalPrice}`);

/* OUTPUT: 
Original Price was: 300, Discount applied: 10%
Final Price is: 270
*/
