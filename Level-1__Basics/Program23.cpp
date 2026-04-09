#include <iostream>
using namespace std;

int main()
{
    double units, rate, total ;
    
    cout << "Enter the Units Consumed : " ;
    cin >> units ;
    cout << "Enter the Rate per Unit : " ;
    cin >> rate ;
    
    total = units * rate ;
    cout << " Total Bill Amount : " << total << endl ;

    return 0;
}
