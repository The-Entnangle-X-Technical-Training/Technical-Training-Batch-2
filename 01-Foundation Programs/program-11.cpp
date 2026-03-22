// Write a program that takes a number as input and displays whether it is positive, negative, or zero.
#include <iostream>
using namespace std;
int main() {
    int number;
    cout<<"Enter your number : ";
    cin>>number;

    if(number>0)
    {
        cout<<number<<" is a positive number.";
    }else if (number<0)
    {
        cout<<number<<" is a negative number.";
    }
    else{
        cout<<number<<" is a Zero.";
    }
    
    return 0;
}