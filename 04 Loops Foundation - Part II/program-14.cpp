// Problem 14: Right Triangle - Same Number in Row
// 1
// 2 2
// 3 3 3
// 4 4 4 4
// Write a program that prints this pattern for N rows.


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
            cout<<i+1<<" ";
        }
        cout<<endl;
        
    }
    
    
    return 0;
}