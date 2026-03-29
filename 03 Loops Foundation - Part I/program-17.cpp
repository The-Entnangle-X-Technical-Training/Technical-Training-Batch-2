// Write a program that checks if a number is a palindrome (reads same forwards and backwards).
// Example: 121, 12321, 1331 are palindromes


#include<iostream>
using namespace std;
int main()
{
    int n,rev=0,digit;
    cout<<"Enter a number : ";
    cin>>n;
    int number=n;
    for (int i = 1; 0 < n; i++)
    {
        digit=n%10;
        rev=(rev*10)+digit;  
        n=n/10;
    
    }
    if (number==rev)
    {
        cout<<number<<" is a palindromes.";
    }else{
        cout<<number<<" is not a palindromes.";
    }
    
    return 0;
}