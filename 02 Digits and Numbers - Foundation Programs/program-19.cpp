// Write a program that takes a 3-digit number, calculates the sum of its digits, and checks if the number is
// divisible by this sum. Example: 153 → 1+5+3=9, 153÷9=17 → Harshad Number. Display "Harshad
// Number" or "Not Harshad Number"


#include<iostream>
using namespace std;
int main()
{
    int number,first_digit,middle_digit,last_digit,sum;
    cout<<"Enter 3-digit number : ";
    cin>>number;
    first_digit=number/100;
    middle_digit=(number/10)%10;
    last_digit=number%10;
    sum=first_digit+middle_digit+last_digit;
    if (number%sum==0)
    {
        cout<<"Harshad Number.";
    }else{
        cout<<"Not Harshad Number.";
    }
    
    return 0;
}