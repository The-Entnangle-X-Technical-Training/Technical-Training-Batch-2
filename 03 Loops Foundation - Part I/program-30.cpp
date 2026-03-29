// Write a program that takes two numbers and finds their LCM.
// Hint: LCM × GCD = Product of two numbers

#include<iostream>
using namespace std;
int main()
{
    int a,b,gcd,lcm,r;
    cout<<"Enter two number : ";
    cin>>a>>b;
    int n1=a;
    int n2=b;
    if (b>a)
    {
        a=a+b;
        b=a-b;
        a=a-b;
    }
    while (b!=0)
    {
        r=a%b;
        a=b;
        b=r;
        gcd=a;
    }
    lcm=(n1*n2)/gcd;
    cout<<"The lcm of "<<n1<<" and "<<n2<<" is : "<<lcm;

    
    


    return 0;
}