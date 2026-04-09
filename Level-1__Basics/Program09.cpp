#include <iostream>
using namespace std;

int main() 
{
    double celcius, fahrenheit ;
    cout << " Enter the temperature in degree Fahrenheit : " ;
    cin >> fahrenheit ;
    celcius = (fahrenheit - 32) * 5/9 ;
    cout << " The temperature in Celcius = " << celcius << endl ;
    return 0;
}
