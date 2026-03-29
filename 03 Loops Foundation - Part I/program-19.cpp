// Write a program that checks if a number is an Armstrong number (sum of cubes of digits equals the
// number itself).
// Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
#include<iostream>
using namespace std;
int main()
{
    int sum_of_cube=0,n,digit;
    cout<<"Enter a number to check Armstrong Number : ";
    cin>>n;
    int copy=n;
    for (int i = 0; 0 < n; i++)
    {
        digit=n%10;
        sum_of_cube=sum_of_cube+(digit*digit*digit);
        n=n/10;
        
    }
    if (sum_of_cube==copy)
    {
        cout<<sum_of_cube<<" is a armstrong number.";
    }else{
        cout<<copy<<" is not a armstrong number.";
    }
    
}