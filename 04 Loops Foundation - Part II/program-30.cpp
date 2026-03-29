// Problem 30: Hollow Pyramid
//    *
//   * *
//  *   *
// * * * *
// Write a program that prints hollow pyramid (only borders have stars) for N rows
#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"Enter row";
    cin>>row;
    for (int i = 1; i <= row; i++)
    {
        for (int j = row; j>i; j--)
        {
            cout<<" ";
        }
        for (int k = 1; k <= i; k++)
        {
            if (i==row||k==1||k==i)
            {
                cout<<"* ";
                
            }else{
                cout<<"  ";
            }
            
        }
        cout<<endl;
        
    }
    
    return 0;
}