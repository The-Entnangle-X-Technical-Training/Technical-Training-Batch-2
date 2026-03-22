// Write a program that takes two numbers as input, swaps them without using any third variable (use
// arithmetic operations), and displays values before and after swapping.
#include <iostream>
using namespace std;
int main() {
    int num1,num2;
    cout<<"Enter two number : ";
    cin>>num1;
    cin>>num2;
    cout<<"number 1 : "<<num1 <<endl<<"number 2 : "<<num2<<endl;
   
    num1=num2+num1;
    num2= num1-num2;
    num1=num1-num2;
    
    cout<<"After swapping, "<<endl<<"number : 1 : "<<num1 <<endl<<"number 2 : " <<num2<<endl;

    return 0;
}