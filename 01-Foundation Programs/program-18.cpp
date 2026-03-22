// Write a program that takes three numbers as input and displays the greatest among them.

#include <iostream>
using namespace std;
int main() {
    
    int num1,num2,num3;
    cout<<"Enter your three number : ";
    cin>>num1>>num2>>num3;
    
    if (num1>num2)
    {
        if (num1>num3)
        {
            cout<<num1<<" is greater.";
        }else{
            cout<<num3<<" is greater.";
        }
        
    }else if (num2>num3)
    {
        cout<<num2<<" is greater."; 
    }else{
        cout<<num3<<" is greater.";
    }
    
    

    return 0;
}