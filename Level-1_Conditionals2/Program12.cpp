#include <iostream>
using namespace std;

int main()
{
    double cost, sell ;
    
    cout << "Enter Cost Price : " ;
    cin >> cost ;
    cout << "Enter Selling Price : " ;
    cin >> sell ;
    
    if (cost> sell) {
        cout << " Loss " ;
    } 
    
    else if (cost < sell) {
      cout << " Profit" ;
    }
    
    else {
      cout << " No Profit No Loss " ;
    }

    return 0;
}
