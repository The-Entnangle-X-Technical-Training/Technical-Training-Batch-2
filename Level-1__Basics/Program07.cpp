#include <iostream>
using namespace std;

int main() 
{
    int p, r, t, SI ;
    cout << "Enter Principle : " ;
    cin >> p ;
    cout << "Enter Rate : " ;
    cin >> r ;
    cout << "Enter Time : " ;
    cin >> t ;
    SI = (p * r * t) / 100 ;
    cout << " Simple Interest = " << SI << endl ;
    return 0;
}
