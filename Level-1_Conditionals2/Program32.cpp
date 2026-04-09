#include <iostream>
using namespace std;

int main()
{
    double income, tax = 0 ;
    
    cout << "Enter your income in Lakhs Per Annum (LPA) " ;
    cin >> income ;
  
    if (income>0 && income < 2.5) {
        tax = 0 ;
    }
    else if (income> 2.5 && income < 5) {
        tax = income * 0.05 ;
    }
    else if (income> 5 && income < 10) {
        tax = income * 0.20 ;
    }
    else {
        tax = income * 0.30 ;
    }
    cout << "Total Tax Amount in Lakhs = " << tax << endl;
    return 0;
}
