#include <iostream>
using namespace std;

int main() 
{
  int num1, num2, num3 ;
    cout << " Enter First Number: ";
    cin >> num1 ;
    cout << "Enter Second Number: " ;
    cin >> num2 ;
    cout << " Enter Third Number: " ;
    cin >> num3 ;
    if (num1> num2 && num1> num3) {
      cout << " First Number is the greatest.";
    }
    if (num2> num1 && num2 > num3) {
      cout << "Second Number is the greatest." ;
    }

    else {
    cout << " Third Number is the greatest. " ;
    }
    return 0 ;
}
