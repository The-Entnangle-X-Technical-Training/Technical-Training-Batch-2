#include <iostream>
using namespace std;

int main() 
{
    double units, total ;
    cout << "Enter units used : " ;
    cin >> units ;
    
    if (units <= 100 ) {
    total = units * 5 ;
    }
    
    else {
    total = units * 7 ;
    }
    
    cout << " Total Amount = " << total << endl ;
    
    return 0 ;
}
