#include <iostream>
using namespace std;

int main() 
{
    int num1, num2, addition, subtraction, multiplication, division, modulus ;
    cout << "Enter First Number: ";
    cin >> num1;
    cout << "Enter Second Number: ";
    cin >> num2;
    addition = num1 + num2;
    cout << " num1 + num2 = " << addition << endl;
    subtraction = num1 - num2;
    cout << " num1 - num2 = " << subtraction << endl;
    multiplication = num1 * num2;
    cout << " num1 * num2 = " << multiplication << endl;
    division = num1 / num2;
    cout << " num1 / num2 = " << division << endl;
    modulus = num1 % num2;
    cout << " num1 % num2 = " << modulus << endl;
    return 0;
}
