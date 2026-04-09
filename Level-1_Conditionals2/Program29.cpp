#include <iostream>
using namespace std;

int main()
{
    int ang1, ang2, ang3 ;
    
    cout << "Enter three angles of a Triangle : " ;
    cin >> ang1 >> ang2 >> ang3 ;
    
    if (ang1< 90 && ang2 <90 && ang3 <90) {
        cout << " This is an Acute Triangle " ;
    }
    else if (ang1 == 90 || ang2 == 90 || ang3 == 90) {
        cout << " This is a right Triangle " ;
    }
    else if (ang1 > 90 || ang2 > 90 || ang3 > 90) {
        cout << " This is an obtuse Triangle " ;
    }
    return 0;
}
