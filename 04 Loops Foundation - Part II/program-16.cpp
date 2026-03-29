// Problem 16: Inverted Right Triangle - Numbers
// 1 2 3 4
// 1 2 3
// 1 2
// 1
// Write a program that prints this inverted pattern for N rows.


#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"Enter row : ";
    cin>>row;
    for (int i = row; 0<i; i--)
    {
        for (int j = 0; j < i; j++)
        {
            cout<<j+1<<" ";
        }
        cout<<endl;
        
    }
    
    

    return 0;
}
