// Write a program that takes a number N and calculates the sum of first N odd numbers.


#include<iostream>
using namespace std;
int main()
{
    int number,sum=0;
    cout<<"Enter a Number N : ";
    cin>>number;
    for (int i = 1; i <= number ; i++)
    {
        if (i%2!=0)
        {
            sum=sum+i;       
            cout<<i<<" + ";     
        }
        
    }
    cout<<"= "<<sum;
   
    return 0;
}

