// Write a program that takes a number N and prints the first N odd numbers (1, 3, 5, 7...)


#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a Number N : ";
    cin>>n;
    for (int i = 1; i<= n; i++)
    {
        if (i%2!=0)
        {
            cout<<i<<", ";
        }
        
    }
    
    return 0;
}