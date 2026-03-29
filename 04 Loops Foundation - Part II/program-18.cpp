// Problem 18: Right Triangle - Stars
// *
// * *
// * * *
// * * * *



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
            cout<<"* ";
            
        }
        cout<<endl;
        
    }
    

    
    return 0;
}
