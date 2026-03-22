// Write a program that takes a number N as input and prints all numbers from 1 to N.

#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a Number N : ";
    cin>>n;
    for (int i = 1; i <= n; i++)
    {
        cout<<i<<", ";
    }
    
    return 0;
}