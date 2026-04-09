#include <iostream>
using namespace std;

int main() 
{
    int dividend, divisor ;
    cout << "Enter Dividend : " ;
    cin >> dividend ;
    cout << " Enter Divisor :" ;
    cin >> divisor ;
    if (dividend % divisor == 0) {
     cout << " Divisible " ;
    }
    else {
      cout << " Not Divisible " ;
    }
    return 0 ;
}
