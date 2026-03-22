// Write a program that takes a number N as input and prints all numbers from N to 1 in reverse order.

#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a Number N : ";
    cin>>n;
    for (int i = n; i >= 1; i--)
    {
        cout<<i<<", ";
    }
    
    return 0;
}