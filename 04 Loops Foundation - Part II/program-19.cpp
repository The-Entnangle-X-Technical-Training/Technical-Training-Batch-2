// Problem 19: Inverted Right Triangle - Stars
// * * * *
// * * *
// * *
// *



#include<iostream>
using namespace std;
int main()
{
    int row;
    cout<<"Enter row : ";
    cin>>row;
    int count=1;
    for (int i = row; 0<i; i--)
    {
        for (int j = i; j>0; j--)
        {
            cout<<"* ";
            
        }
        cout<<endl;
        
    }
    

    
    return 0;
}
