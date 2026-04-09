#include <iostream>
using namespace std;

int main()
{
    int num, lastDigit;

    cout << "Enter a number: ";
    cin >> num;

    lastDigit = num % 10;   

    cout << "Last digit = " << lastDigit << endl;

    return 0;
}
