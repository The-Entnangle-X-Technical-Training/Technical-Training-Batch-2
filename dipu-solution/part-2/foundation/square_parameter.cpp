#include <iostream>
using namespace std;

int main() {
    double side;
    cout << "Enter the side of the square: ";
    cin >> side;

    double area = side * side;
    double perimeter = 4 * side;

    cout << "Area of the square: " << area << endl;
    cout << "Perimeter of the square: " << perimeter << endl;

    return 0;
}