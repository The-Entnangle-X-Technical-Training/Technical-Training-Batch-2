#include <iostream>
using namespace std;

int main() 
{
    double side, perimeter, area ;
    cout << " Enter the side of the square : " ;
    cin >> side ;
    perimeter = side * 4 ;
    cout << " Perimeter of the square = " << perimeter << endl ;
    area = side * side ;
    cout << " Area of the square = " << area << endl ;
    return 0;
}
