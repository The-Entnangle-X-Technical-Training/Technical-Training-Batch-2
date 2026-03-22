// Write a program that takes a 3-digit number as input and extracts and displays the first digit.
#include<iostream>
using namespace std;
int main()
{
    int number,first_digit;
    cout<<"Enter 3-digit number : ";
    cin>>number;
    
    first_digit=number/100;

    cout<<"The First Digit is : "<<first_digit;

    return 0;
}