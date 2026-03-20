// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int main() {
    // Write C++ code here
    int num1,num2;
    int temp;
    cout<<"Enter two number : ";
    cin>>num1;
    cin>>num2;
    cout<<"Your two number is, number 1 : "<<num1 <<" and number 2 : "<<num2<<endl;
    temp=num1;
    num1=num2;
    num2=temp;
    cout<<"After swapping, number : 1 : "<<num1 <<" and number 2 : " <<num2<<endl;
    

    return 0;
}