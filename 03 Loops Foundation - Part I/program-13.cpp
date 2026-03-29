// Write a program that takes a number and counts how many digits it has using a loop.
// Hint: Keep dividing by 10 until number becomes 0



#include<iostream>
using namespace std;
int main()
{
    int n,digit;
    cout<<"Enter a number : ";
    cin>>n;
    int count=0;
    for (int i = 1; 0 < n; i++)
    {
        n=n/10;
        count++;
        
    }
    cout<<"The digit is : "<<count;
   
    
    return 0;
}