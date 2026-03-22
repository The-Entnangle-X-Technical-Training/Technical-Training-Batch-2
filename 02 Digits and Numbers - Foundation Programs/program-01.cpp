// Write a program that takes any number as input and extracts and displays the last digit of that number.
#include<iostream>
using namespace std;
int main()
{
    int number,last_digit;
    cout<<"Enter any number : ";
    cin>>number;
    
    last_digit=number%10;
    
    cout<<"The Last Digit is : "<<last_digit;
 
    return 0;
}