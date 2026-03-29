// Write a program that takes a number N and prints the first N terms of Fibonacci series (0, 1, 1, 2, 3, 5,
// 8...).
// Hint: Each term is sum of previous two terms

#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a number N : ";
    cin>>n;
    int a=0;
    int b=1;
    if (n<1)
    {
        cout<<"invalid number";
        
    }

    cout<<a<<","<<b<<",";
    for (int i = 2; i < n; i++)
    {

        int c=a+b;
        a=b;
        b=c;

        cout<<c<<",";
        
        
    }
    
}