// Problem 15: Right Triangle - Reverse Numbers
// 1
// 2 1
// 3 2 1
// 4 3 2 1
// Write a program that prints this pattern for N rows

#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"Enter row : ";
    cin>>row;
    for (int i = 0; i < row; i++)
    {
        for (int j = i+1; 0<j; j--)
        {
            cout<<j<<" ";
        }
        cout<<endl;
    }
    

    return 0;
}
