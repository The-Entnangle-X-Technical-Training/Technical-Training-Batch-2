// Write a program that takes a number N and calculates the sum of all its divisors (excluding N itself).
// Example: Divisors of 12 are 1, 2, 3, 4, 6, so sum = 16

#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a Number N : ";
    cin>>n;
    int sum=0;
    for (int i = 1; i <= n/2; i++)
    {
        if (n%i==0)
        {
            cout<<i<<",";
            sum=sum+i;
        }
        
    }
    cout<<endl<<"The sum of all its divisors : "<<sum;
    
    return 0;
}