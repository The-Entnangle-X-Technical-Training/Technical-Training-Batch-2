#include<iostream>
using namespace std;
int main (){
    double celsicus;
    cout << "Enter the celsius = ";
    cin >> celsicus;

    double fahrenheit = (celsicus * 9.0 / 5.0) + 32;

    cout << "Temperature convert to celsicus to fahrenheit = " << fahrenheit <<"" ;
}