#include <iostream>
using namespace std;

int main()
{
    double ang1, ang2, ang3 ;
    
    cout << "Enter three angles : " ;
    cin >> ang1 >> ang2 >> ang3 ;
    
    if (ang1+ ang2+ ang3 == 180) {
        cout << " Valid Triangle" ;
    } 
    
    else {
      cout << " Invalid Triangle" ;
    }

    return 0;
}
