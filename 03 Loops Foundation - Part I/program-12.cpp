// Write a program that takes N and calculates the sum: 1² + 2² + 3² + ... + N².


#include<iostream>
using namespace std;
int main()
{
    int n ,result=0;
    cout<<"Enter N : ";
    cin>>n;
    for (int i = 1; i <= n; i++)
    {
        result=result+(i*i);
        cout<<i<<"^2 + ";
    }
    cout<<" = "<<result;
    cout<<endl<<"The result is : "<<result;
    
    return 0;
}