#include <iostream>
using namespace std;

int main()
{
    double p, r, t, SI, total ;
    
    cout << "Enter Principal Amount : " ;
    cin >> p ;
    cout << "Enter the Rate of Interest : " ;
    cin >> r ;
    cout << "Enter the Time Period : " ;
    cin >> t ;
    
    SI = (p * r * t) / 100 ;
    cout << "Simple Interest : " << SI << endl ;
    total = (p + SI) ;
    cout << " Total Amount : " << total << endl ;

    return 0;
}
