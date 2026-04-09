#include <iostream>
using namespace std;

int main()
{
    double units, bill ;
    
    cout << "Enter Number of Units used : " ;
    cin >> units ;
    
    if (units >= 0 && units <= 100) {
        bill = units * 5 ;
        cout << " Total Bill Amount = " << bill << endl ;
    }
    else if (units >= 101 && units <= 200) {
        bill = units * 7 ;
        cout << " Total Bill Amount = " << bill << endl ;
    }
    else if (units >= 201 && units <= 300) {
        bill = units * 10 ;
        cout << " Total Bill Amount = " << bill << endl ;
    }
    else {
        bill = units * 15 ;
        cout << " Total Bill Amount = " << bill << endl ;
    }

    return 0;
}
