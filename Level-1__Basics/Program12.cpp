#include <iostream>
using namespace std;

int main() 
{
    double base, height, area ;
    cout << " Enter the base of the triangle : " ;
    cin >> base ;
    cout << " Enter the height of the triangle : " ;
    cin >> height ;
    area = (base * height) / 2 ;
    cout << " Area of the triangle = " << area << endl ;
    return 0;
}
