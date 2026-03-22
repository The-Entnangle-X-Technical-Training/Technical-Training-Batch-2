/*--------------------------------
Problem 16: Days to Years, Weeks, Days Converter

Write a program that takes total number of days as input and converts it into years, weeks, and remaining
days, then displays all three values.
--------------------------------*/

// var remainder = 800 % 365;
// // 70
// var subRemainderFromOriginal = 800 - remainder;
// // 730
// var divBy365 = subRemainderFromOriginal / 365;
// // 2

// console.log(divBy365);

var n = 115;
var years = (n / 365 + "")[0] * 1;
var convDays = years * 365;
var remDays = n - convDays;
var weeks = ((remDays / 7 + "")[0] + (remDays / 7 + "")[1]) * 1;
var weekDays = weeks * 7;
var days = remDays - weekDays;

console.log(`Total Days Given: ${n},`);
console.log(`Years: ${years}, Weeks: ${weeks}, Days:${days}`);

/* OUTPUT:
Total Days Given: 115,
Years: 0, Weeks: 16, Days:3
*/
