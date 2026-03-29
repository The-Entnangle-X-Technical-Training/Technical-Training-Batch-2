// Write a program that takes a number N and counts how many prime numbers exist from 1 to N.

#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a number N : ";
    cin>>n;
    int counter=0;
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
            counter++;
        }
        
    }
    cout<<"Total prime number between 1 to "<<n<<" is : "<<counter;
    return 0;
}