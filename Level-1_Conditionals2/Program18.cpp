#include <iostream>
using namespace std;

int main()
{
    int side1, side2, side3 ;
    
    cout << "Enter three sides of a Triangle: " ;
    cin >> side1 >> side2 >> side3 ;
    
    if ((side1+side2 > side3) &&
       (side2+side3 > side1) &&
       (side1+side3 > side2)) {
        cout << " Valid " ;
    } 
    
    else {
      cout << " Invalid " ;
    }

    return 0;
}
