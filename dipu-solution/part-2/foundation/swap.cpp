#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cout << "Enter first number (a): ";
    cin >> a;
    cout << "Enter second number (b): ";
    cin >> b;
    cout << "Enter third number (c): ";
    cin >> c;

    cout << "Original numbers: a = " << a << ", b = " << b << ", c = " << c << endl;

    int temp = a;
    a = c;
    c = b;
    b = temp;

    cout << "Numbers after swap: a = " << a << ", b = " << b << ", c = " << c << endl;

    return 0;
}