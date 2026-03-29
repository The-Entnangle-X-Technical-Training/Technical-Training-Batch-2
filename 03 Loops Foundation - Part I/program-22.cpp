// Write a program that takes a number and checks whether it is prime or not using a loop.
// Hint: Check if the number has any divisor from 2 to N-1

#include<iostream>
using namespace std;
int main()
{
    int N;
    cout<<"Enter a number : ";
    cin>>N;
    int isPrime=0;
    for (int i = 2; i < N; i++)
    {
        if (N%i==0)
        {
            isPrime++;
            break;
        }
        
    }
    if (isPrime==0)
    {
        cout<<"The Number "<<N<<" is a Prime number.";
    }else{
        cout<<"This is not a prime number.";
    }
    
    
    return 0;
}