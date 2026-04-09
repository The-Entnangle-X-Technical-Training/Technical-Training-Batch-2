#include <iostream>
using namespace std;

int main()
{
    int num1, num2, num3 ;
    
    cout << "Enter three numbers : " ;
    cin >> num1 >> num2 >> num3 ;
    
    if (num1 > num2 && num2 > num3) {
        cout << " Descending Order " ;
    }
    else if (num1 < num2 && num2 < num3) {
        cout << " Ascending Order " ;
    }
    else {
        cout << " Neither Ascending Nor Desceding " ;
    }
    return 0;
}
