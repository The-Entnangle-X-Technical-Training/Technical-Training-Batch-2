#include <iostream>
using namespace std;

int main()
{
    int age, price=0 ;
    
    cout << "Enter your age " ;
    cin >> age ;
  
    if (age>=0 && age<=12) {
        price = 100 ;
    }
    else if (age>=13 && age<=17) {
        price = 150 ;
    }
    else if (age>=18 && age<=59) {
        price = 200 ;
    }
    else {
        price = 120 ;
    }
    cout << "Total Ticket Price = " << price << endl;
    return 0;
}
