#include <iostream>
using namespace std;

int main()
{
    double cost, percent, discount, total ;
    
    cout << "Enter Original Cost of the Product : " ;
    cin >> cost ;
    cout << "Enter Discount Percent : " ;
    cin >> percent ;
    
    discount = cost * (percent / 100) ;
    total = cost - discount ;
    cout << " Final amount after applying discount : " << total << endl ;
    
    return 0;
}
