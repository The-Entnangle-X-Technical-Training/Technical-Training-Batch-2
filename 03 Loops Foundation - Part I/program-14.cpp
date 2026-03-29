// Write a program that takes a number and calculates the sum of its digits using a loop.
// Hint: Extract last digit using %10, add to sum, remove last digit using /10


#include<iostream>
using namespace std;
int main()
{
    int n,digit,sum=0;
    cout<<"Enter a number : ";
    cin>>n;
    
    for (int i = 1; 0 < n; i++)
    {
        sum=sum+(n%10);
        n=n/10;
        
        
    }
    cout<<"The sum of its digit is : "<<sum;
   
    
    return 0;
}