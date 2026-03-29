// Write a program that takes a number and counts how many even digits and how many odd digits it
// contains.


#include<iostream>
using namespace std;
int main()
{
    int n,sum=0,digit,even_count=0,odd_count=0;
    cout<<"Enter a Number N : ";
    cin>>n;
    for (int i = 1; 0 < n; i++)
    {
        digit=n%10;
        if (digit%2==0)
        {
            even_count++;
        }else
        {
            odd_count++;
        }
         
        n=n/10;
    
    }

    cout<<"Even digit are : "<<even_count<<endl;
    cout<<"Odd digit are : "<<odd_count<<endl;
   
    return 0;
}
