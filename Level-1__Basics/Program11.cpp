#include <iostream>
using namespace std;

int main() 
{
    double radius, area, pi ;
    cout << " Enter the radius of the circle : " ;
    cin >> radius ;
    pi = 3.14159 ;
    area = radius * radius * pi ;
    cout << " Area of the circle = " << area << endl ;
    return 0;
}
