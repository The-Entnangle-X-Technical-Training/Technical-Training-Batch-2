// Write a program that takes a number and finds the largest digit in it using a loop
#include<iostream>
using namespace std;
int main()
{
    int n,largest,digit;
    cout<<"Enter a number : ";
    cin>>n;
    largest=0;
    for (int i = 0; 0 < n; i++)
    {
        digit=n%10;
        if (digit>largest)
        {
            largest=digit;
        }
        n=n/10;
        
    }
    cout<<"The largest digit is : "<<largest;
    
    return 0;
}