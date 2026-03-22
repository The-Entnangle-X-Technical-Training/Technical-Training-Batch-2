// Write a program that takes a number N and prints its multiplication table from 1 to 10


#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter a Number N : ";
    cin>>n;
    for (int i = 1; i<= 10; i++)
    {
       cout<<n<<" x "<<i<<" = "<<i*n<<endl;
        
    }
    
    return 0;
}