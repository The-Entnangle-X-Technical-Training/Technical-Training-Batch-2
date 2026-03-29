// Write a program that takes a number as input and prints all its factors using a loop.
#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"enter a numer : ";
    cin>>n;
    for (int i = 1; i*i < n; i++)
    {
        if (n%i==0)
        {
            cout<<i<<" x "<<n/i<<endl;
        }
        
    }
    
    return 0;
}