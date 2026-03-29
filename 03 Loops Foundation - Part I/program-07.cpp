// Write a program that takes a number N and calculates the sum of first N natural numbers (1 + 2 + 3 + ... +
// N).
#include<iostream>
using namespace std;
int main()
{
    int number,sum=0;
    cout<<"Enter a Number N : ";
    cin>>number;
    for (int i = 1; i < number ; i++)
    {
        cout<<i<<" + ";
        sum=sum+i;
    }
    sum=sum+number;
    cout<<number<<" = "<<sum;
    cout<<endl<<"The Sum of first "<<number<<" natural numbers : "<<sum;
    return 0;
}