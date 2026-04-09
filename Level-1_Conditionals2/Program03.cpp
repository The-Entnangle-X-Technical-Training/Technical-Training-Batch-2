#include <iostream>
using namespace std;

int main() 
{
    int num1, num2  ;
    cout << "Enter First Number : " ;
    cin >> num1 ;
    cout << " Enter Second Number :" ;
    cin >> num2 ;
    if (num1 > num2) {
     cout << " First Number is Greater " ;
    }
    else if (num1 < num2) {
     cout << " Second Number is Greater " ;
    }
    else {
      cout << " Both are equal " ;
    }
    return 0 ;
}
