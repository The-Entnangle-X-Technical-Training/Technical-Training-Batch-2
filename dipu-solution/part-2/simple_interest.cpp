#include<iostream>
using namespace std;
int main(){
    
    int p, r, t;
    cout << "Enter the principal amount = ";
    cin >> p;
    cout << "Enter the rate of amount = ";
    cin >> r;
    cout << "Enter the time = ";
    cin >> t;

    float si = (p * r * t) / 100;

    cout << "Simple interest of = " << si << endl;

}