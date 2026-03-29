// Problem 12: Sum of Series: 1 - 2 + 3 - 4 + 5 - 6 + ... ± N
// Write a program that calculates this alternating series.


#include<iostream>
using namespace std;
int main()
{
    int n,sum=0;;
    cout<<"Enter N : ";
    cin>>n;

    for (int i = 1; i <= n; i++)
    {
        if (i%2==0)
        {
            sum=sum-(i);
        }
        else
        {
            sum=sum+(i);
        }
    }
    cout<<"alternating sum of series = "<<sum;
    return 0;
}