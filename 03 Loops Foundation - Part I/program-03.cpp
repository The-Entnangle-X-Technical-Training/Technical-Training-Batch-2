// Write a program that takes a number N and prints the first N even numbers (2, 4, 6, 8...).


#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a Number N : ";
    cin>>n;
    for (int i = 2; i<= n; i++)
    {
        if (i%2==0)
        {
            cout<<i<<", ";
        }
        
    }
    
    return 0;
}