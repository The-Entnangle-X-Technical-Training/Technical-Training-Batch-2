#include <iostream>
using namespace std;

int main() 
{
    int temp  ;
    cout << "Enter temperature in Celcius : " ;
    cin >> temp ;
    
    if (temp < 15 ) {
     cout << " Cold " ;
    }
    if ( temp >= 15 && temp <= 30 ) {
    cout << " Normal " ;
    }
    if ( temp > 30 ) {
    cout << " Hot " ;
    }
    return 0 ;
}
