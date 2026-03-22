// Write a program that takes a 3-digit number as input and extracts and displays the middle digit.

#include<iostream>
using namespace std;
int main()
{
    int number,middle_digit;
    cout<<"Enter 3-digit number : ";
    cin>>number;
    
    middle_digit=(number/10)%10;

    cout<<"The Middle Digit is : "<<middle_digit;

    return 0;
}