// Problem 13: Right Triangle - Numbers (Rows)
// 1
// 1 2
// 1 2 3
// 1 2 3 4
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
        for (int j = 0; j < i+1; j++)
        {
            cout<<j+1<<" ";
        }
        cout<<endl;
    
    }
    


    return 0;
}