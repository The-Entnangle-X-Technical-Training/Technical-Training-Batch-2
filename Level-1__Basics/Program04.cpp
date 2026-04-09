#include <iostream>
using namespace std;

int main() 
{
    double num1, num2, num3, sum, avg ;
    cout << "Enter First Number: ";
    cin >> num1;
    cout << "Enter Second Number: ";
    cin >> num2;
    cout << "Enter Third Number: ";
    cin >> num3;
    sum = num1 + num2 + num3;
    cout << " The sum of these three numbers is: " << sum << endl;
    avg = sum / 3 ;
    cout << " The average of these three numbers is: " << avg << endl;
    return 0;
}
