#include <iostream>
using namespace std;

int main() 
{
    double length, width, area, perimeter ;
    cout << " Enter the length of the rectangle : " ;
    cin >> length ;
    cout << " Enter the width of the rectangle : " ;
    cin >> width ;
    area = length * width ;
    cout << " Area of the given rectangle = " << area << endl ;
    perimeter = 2 * (length + width) ;
    cout << "Perimeter of the given rectangle = " << perimeter << endl ;
    return 0;
}
