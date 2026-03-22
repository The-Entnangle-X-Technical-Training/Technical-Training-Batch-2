#include<iostream>
using namespace std;
int main(){
    int num;
    cout << "Enter the number for check which type of number = ";
    cin >> num;

    if (num > 0)
    {
        cout << "These number is positive number ";
    }
    else if (num < 0)
    {
        cout << "These number us negative number ";
    }
    else{
        cout << "These number is zero ";

    }
}