#include<iostream>
using namespace std;
int main (){
    int a, b, c;
    cout << "Enter the first number = ";
    cin >> a;
    cout << "Enter the second number = ";
    cin >> b;
    cout << "Enter the third number = ";
    cin >> c;

    float avg = (a + b + c)/3.0;
    
    cout << "Average of three number = " << avg << endl;
}