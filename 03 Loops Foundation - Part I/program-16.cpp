// Write a program that takes a number and calculates the product of all its digits using a loop.


#include<iostream>
using namespace std;
int main()
{
    int n,product=1;
    cout<<"Enter a number : ";
    cin>>n;
    
    for (int i = 1; 0 < n; i++)
    {
        product=product*(n%10);
        n=n/10;
        
        
    }
    cout<<"The product of its digit is : "<<product;
   
    
    return 0;
}