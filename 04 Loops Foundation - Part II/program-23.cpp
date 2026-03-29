// Problem 23: Palindrome Number Pattern
// 1
// 121
// 12321
// 1234321
// Write a program that prints palindrome number pattern for N rows.
#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"Enter row : ";
    cin>>row;

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < i+1; j++)
        {
            cout<<j+1;
        }
        for (int j = i; 1 <= j ; j--)
        {
            cout<<j;
        }
        cout<<endl;
        
    }
    

    return 0;
}