// Write a program that takes a 3-digit number as input and calculates the product of all its digits, then
// displays the result.


#include<iostream>
using namespace std;
int main()
{
    int number,first_digit,middle_digit,last_digit,product;
    cout<<"Enter 3-digit number : ";
    cin>>number;
    first_digit=number/100;
    middle_digit=(number/10)%10;
    last_digit=number%10;
    product=first_digit*middle_digit*last_digit;

    cout<<"The product of all its digits : "<<product;

    return 0;
}