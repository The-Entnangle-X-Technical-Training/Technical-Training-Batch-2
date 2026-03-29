// Problem 20: Pyramid - Stars (Centered)
//    *
//   * *
//  * * *
// * * * *
// Write a program that prints centered pyramid with stars for N rows

#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"Enter row : ";
    cin>>row;

    for (int i = 1; i <= row; i++)
    {
        for (int j = row; j > i; j--)
        {
            cout<<" ";
            
        }
        for (int k = 0; k < i; k++)
        {
            cout<<"* ";
        }
        cout<<endl;
        
    }
    
    return 0;
}