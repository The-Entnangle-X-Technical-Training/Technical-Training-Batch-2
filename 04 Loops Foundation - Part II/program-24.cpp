// Problem 24: Number Pyramid (Centered)
//    1
//   1 2
//  1 2 3
// 1 2 3 4
// Write a program that prints this centered number pyramid for N rows.
#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"Enter row : ";
    cin>>row;

    for (int i = 1; i <= row; i++)
    {
        for (int j = row; j>i; j--)
        {
            cout<<" ";
        }
        for (int k = 0; k < i; k++)
        {
            cout<<k+1<<" ";
        }
        cout<<endl;
        
    }
    
    return 0;
}