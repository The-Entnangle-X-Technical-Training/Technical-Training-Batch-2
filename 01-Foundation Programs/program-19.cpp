// Write a program that takes three numbers as input and displays the smallest among them.

#include <iostream>
using namespace std;
int main() {
    
    int num1,num2,num3;
    cout<<"Enter your three number : ";
    cin>>num1>>num2>>num3;
    
    if (num1<num2)
    {
        if (num1<num3)
        {
            cout<<num1<<" is smallest.";
        }else{
            cout<<num3<<" is smallest.";
        }
        
    }else if (num2<num3)
    {
        cout<<num2<<" is smallest."; 
    }else{
        cout<<num3<<" is smallest.";
    }
    
    

    return 0;
}