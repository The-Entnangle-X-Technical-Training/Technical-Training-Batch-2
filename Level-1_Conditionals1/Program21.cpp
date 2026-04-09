#include <iostream>
using namespace std;

int main() 
{
    int ang1, ang2, ang3 ;
    cout << "Enter First Angle : " ;
    cin >> ang1 ;
    cout << "Enter Second Angle : " ;
    cin >> ang2 ;
    cout << "Enter Third Angle : " ;
    cin >> ang3 ;
    
    if (ang1+ang2+ang3 == 180 ) {
    cout << " Valid " ;
    }
    
    else {
    cout << " Invalid " ;
    }
    
    return 0 ;
}
