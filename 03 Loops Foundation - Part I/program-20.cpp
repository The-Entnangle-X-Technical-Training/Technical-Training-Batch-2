// write a program that checks if a number is a strong number (sum of factorial of digits equals the number).
// Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145

#include<iostream>
using namespace std;
int main()
{
    int n,fact=1,digit,sum_fact=0;
    cout<<"Enter a number to check is strong number : ";
    cin>>n;
    int copy=n;

    for (int i = 0; 0 < n; i++)
    {
        fact=1;
        digit=n%10;
        for (int i = 1; i <= digit ; i++)
        {
            fact=fact*i;
        }
        sum_fact=sum_fact+fact;
        
        n=n/10;
    }
    if (sum_fact==copy)
    {
        cout<<sum_fact<<" is a strong number.";
    }else{
        cout<<copy<<" is not a strong number.";
    }
    
    
    return 0;
}
