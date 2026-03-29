// Write a program that takes a number and prints it in reverse using a loop.
// Hint: Extract digits one by one and build reversed number


#include<iostream>
using namespace std;
int main()
{
    int n,rev=0,digit;
    cout<<"Enter a number : ";
    cin>>n;
    
    for (int i = 1; 0 < n; i++)
    {
        digit=n%10;
        rev=(rev*10)+digit;  
        n=n/10;
    
    }
    cout<<"The number is after reversed : "<<rev;
    return 0;
}