#include <iostream>
using namespace std;

int main() 
{
    double celcius, fahrenheit ;
    cout << " Enter the temperature in degree Celcius : " ;
    cin >> celcius ;
    fahrenheit = (celcius * 9/5) + 32 ;
    cout << " The temperature in Fahrenheit = " << fahrenheit << endl ;
    return 0;
}
