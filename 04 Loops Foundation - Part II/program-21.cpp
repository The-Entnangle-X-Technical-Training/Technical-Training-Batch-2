// Problem 21: Inverted Pyramid - Stars
// * * * *
//  * * *
//   * *
//    *
#include<iostream>
using namespace std;
int main(){
    int row;
    cout<<"Enter row : ";
    cin>>row;
    for (int i = row; 1<=i; i--)
    {
        for (int j = i; j < row; j++)
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