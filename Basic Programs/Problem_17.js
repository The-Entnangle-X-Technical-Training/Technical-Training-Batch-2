/*--------------------------------
Problem 17: Seconds to Hours:Minutes:Seconds Converter

Write a program that converts total seconds into hours, minutes, and seconds format and displays the
result.
--------------------------------*/

const givenSec = 3786;
const hour = (givenSec / 3600 + "")[0] * 1;
const remSec = givenSec % 3600;
const min = (remSec / 60 + "")[0] * 1;
const secondsLeft = remSec % 60;

console.log(`Total seconds: ${givenSec}`);
console.log(`HOUR:MINUTES:SECONDS`);
console.log(`${hour}hr:${min}min:${secondsLeft}sec`);

/* OUTPUT:
Total seconds: 3786
HOUR:MINUTES:SECONDS
1hr:3min:6sec
*/
