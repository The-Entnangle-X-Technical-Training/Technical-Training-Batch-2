// Write a program that takes two numbers base and exponent, and calculates base^exponent using a loop
// (without using pow function).

#include<iostream>
using namespace std;
int main()
{
    int base,exponent,pow=1;
    cout<<"Enter a Base : ";
    cin>>base;
    cout<<"Enter the exponent : ";
    cin>>exponent;
    
    for (int i = 1; i <= exponent ; i++)
    {
       pow=pow*base;
        
    }
    cout<<"The answer is : "<<pow;
    
    return 0;
}
