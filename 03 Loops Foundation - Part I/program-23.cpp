// Write a program that takes a number N and prints all prime numbers from 1 to N.
#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a number N : ";
    cin>>n;
    
    for (int i = 1; i <= n; i++)
    {
        int isPrime=0;
        for (int j = 2; j < i; j++)
        {
            if (i%j==0)
            {
                isPrime=1;
                break;
            }
               
        }
        if (isPrime==0)
        {
            cout<<i<<" ";
        }
        
    }
    
    return 0;
}