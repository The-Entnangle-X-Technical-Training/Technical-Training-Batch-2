// Write a program that takes two numbers as input and displays which one is greater, or if they are equal

#include <iostream>
using namespace std;
int main() {
    int num1,num2;
    cout<<"Enter your two number : ";
    cin>>num1>>num2;

    if (num1==num2)
    {
        cout<<"they are Equal.";
    }else if (num1>num2)
    {
        cout<<"Number 1 is greater.";   
    }else{

        cout<<"Number 2 is greater.";
    }
    

    return 0;
}