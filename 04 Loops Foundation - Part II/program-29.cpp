// Problem 29: Right Triangle - Numbers (Continuous)
// 1
// 2 3
// 4 5 6
// 7 8 9 10
// Write a program that prints continuous numbers in triangle pattern.



#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"Enter row : ";
    cin>>row;
    int count=1;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < i+1; j++)
        {
            cout<<count <<" ";
            count++;
        }
        cout<<endl;
        
    }
    return 0;
}
