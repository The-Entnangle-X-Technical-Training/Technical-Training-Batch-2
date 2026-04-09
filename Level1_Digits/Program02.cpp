#include <iostream>
using namespace std;

int main()
{
    int num, extract ;

    cout << "Enter a number: ";
    cin >> num;

    extract = num / 10;   

    cout << "The number after removing the last digit is : " << extract << endl;

    return 0;
}
