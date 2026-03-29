// Write a program that takes two numbers N and M. Count how many multiples of M exist from 1 to N.
// Example: If N=20 and M=3, multiples are 3, 6, 9, 12, 15, 18, so count = 6

#include<iostream>
using namespace std;
int main() 
{
    int n,m,count=0;
    cout<<"Enter N= ";
    cin>>n;
    cout<<"Enter M= ";
    cin>>m;
    if (m==0)
    {
        cout<<"Can't be multiples of M exits.";
    }else
    {
        cout<<"Multiples are : ";
        for (int i = 1; i <= n/m; i++)
        {
            
            cout<<m*i<<" ";

        }
        cout<<" so count = "<<n/m;
        
    }
    
    
    return 0;
}