// Problem 28: Sum of Series: 1² - 2² + 3² - 4² + ... ± N²
// Write a program that calculates alternating sum of squares.

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
            sum=sum-(i*i);
        }
        else
        {
            sum=sum+(i*i);
        }
    }
    cout<<"alternating sum of squares = "<<sum;
    return 0;
}