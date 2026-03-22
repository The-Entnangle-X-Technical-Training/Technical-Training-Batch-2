// Write a program that takes three numbers (a, b, c) and swaps them cyclically (a→b, b→c, c→a) using
// temporary variables.
#include<iostream>
using namespace std;
int main()
{
    int a,b,c,temp;
    cout<<"Enter three number (a,b,c) : ";
    cin>>a>>b>>c;
    cout<<"Before swap,"<<endl<<a<<"->"<<b<<"->"<<c<<endl;

    temp=a;
    a=b;
    b=c;
    c=temp;
    
    cout<<"After swap, "<<endl<<a<<"->"<<b<<"->"<<c;
    return 0;
}