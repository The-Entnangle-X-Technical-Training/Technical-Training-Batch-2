// Problem 11: Sum of Series: 1 + 1/2 + 1/3 + ... + 1/N
// Write a program that calculates the sum of the harmonic series up to N terms.

#include<iostream>
using namespace std;
int main(){
    int n;
    double sum=0;
    cout<<"Enter the N: ";
    cin>>n;
    for (double i = 1; i <= n; i++)
    {
        cout<<"1/"<<i<<"+";
        sum=sum+(1/i);
    }
    cout<<endl<<"The sum of the harmonic series up to "<<n<<" terms = "<<sum;
    return 0;
}