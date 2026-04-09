#include <iostream>
using namespace std;

int main()
{
    double price, quantity, tax_percent, sub_total, tax_amount, total ;
    
    cout << "Enter Original Price : " ;
    cin >> price ;
    cout << "Enter the Quantity : " ;
    cin >> quantity ;
    cout << " Enter the Tax Percent : " ;
    cin >> tax_percent ;
    
    sub_total = price * quantity ;
    tax_amount = (sub_total * tax_percent) / 100 ;
    total = sub_total + tax_amount ;
    
    cout << " Sub Total : " << sub_total << endl ;
    cout << " Tax Amount : " << tax_amount << endl ;
    cout << " Final Total Amount : " << total << endl ;
    return 0;
}
