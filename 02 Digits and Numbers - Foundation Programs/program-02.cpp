// Write a program that takes a number as input and displays the number after removing its last digit.

#include<iostream>
using namespace std;
int main()
{
    int number,rem_last_digit;
    cout<<"Enter any number : ";
    cin>>number;
    
    rem_last_digit=number/10;
    
    cout<<"After removeing the last digit the number is : "<<rem_last_digit;
 
    return 0;
}