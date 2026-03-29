// write a program that checks if a number is a perfect number (sum of its divisors excluding itself equals
// the number).
// Example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14


#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a Number N : ";
    cin>>n;
    int sum=0;
    for (int i = 1; i <= n/2; i++)
    {
        if (n%i==0)
        {
            // cout<<i<<",";
            sum=sum+i;
        }
        
    }
    if (sum==n)
    {
        cout<<sum<<" is a perfect number.";
    }else{
        cout<<n<<" is not a perfect nuber.";
    }
    
    
    
    return 0;
}