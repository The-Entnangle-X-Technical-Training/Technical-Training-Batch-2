#include <iostream>
using namespace std;

int main()
{
    int a, b, c, D ;
    
    cout << "Enter the coefficients a, b, c of equation ax^2+bx+c=0 : " ;
    cin >> a >> b >> c ;
    
    D = ((b*b) - 4*a*c) ;
    if ( D > 0) {
        cout << " Real and Distinct Roots " ;
    }
    else if (D==0) {
        cout << " Real and Equal Roots " ;
    }
    else {
        cout << " Imaginary Roots " ;
    }
    return 0;
}
