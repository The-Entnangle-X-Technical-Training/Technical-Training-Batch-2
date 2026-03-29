// Write a program that takes two numbers and finds their GCD using a loop.
// Hint: Use Euclidean algorithm - keep dividing until remainder becomes 0

#include<iostream>
using namespace std;
int main()
{
    int a,b,small,gcd,r,temp;
    cout<<"Enter a and b: ";
    cin>>a>>b;
    if(b>a){
        temp=a;
        a=b;
        b=temp;
    }
   
        while (b!=0)
        {
            r=a%b;
            a=b;
            b=r;
            
        }
        cout<<"The GCD is : "<<a;
        
       
        
   //normal method;..

    // for (int i = 1; i <= small/2; i++)
    // {
    //     if (a%i==0 && b%i==0)
    //     {
    //         gcd=i;
    //     }
        
    // }
    // cout<<"GCD is : "<<gcd;
    
    return 0;
}
