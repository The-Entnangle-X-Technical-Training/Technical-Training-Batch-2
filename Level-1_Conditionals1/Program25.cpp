#include <iostream>
using namespace std;

int main() 
{
    int amount, total  ;
    cout << "Enter Amount : " ;
    cin >> amount ;
    
    if (amount >= 1000) {
     total = amount * 0.90 ;
     cout << "Total Amount After Discount = " << total << endl ;
    }
    else {
     total = amount ;
     cout << "No discount. Total Amount =" << total << endl ;
    }
    
    return 0 ;
}
