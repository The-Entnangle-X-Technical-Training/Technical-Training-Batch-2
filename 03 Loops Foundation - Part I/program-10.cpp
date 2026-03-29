// Write a program that takes a number N and calculates its factorial (N! = 1 × 2 × 3 × ... × N).


#include<iostream>
using namespace std;
int main()
{
    int number,fact=1;
    cout<<"Enter a Number N : ";
    cin>>number;
    for (int i = 1; i <= number ; i++)
    {
       
            fact=fact*i;       
            cout<<i<<" x ";     
        
        
    }
    cout<<"= "<<fact;
   
    return 0;
}
