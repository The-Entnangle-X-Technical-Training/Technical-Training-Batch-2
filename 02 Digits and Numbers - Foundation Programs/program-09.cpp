// Write a program that takes a 4-digit number and calculates the average of its first and last digits.

#include<iostream>
using namespace std;
int main()
{
    int number,first_digit,last_digit,avg;
    cout<<"Enter 4-digit number : ";
    cin>>number;
    
    last_digit=number%10;  
    first_digit=number/1000;
    avg=(first_digit+last_digit)/2;

    cout<<"First Digit : "<<first_digit<<endl<<"last digit : "<<last_digit<<endl;
    cout<<"The average of its first and last digits : "<<avg;

    return 0;
}