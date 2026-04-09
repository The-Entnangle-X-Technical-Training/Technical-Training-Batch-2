#include <iostream>
using namespace std;

int main()
{
    int age, income, credit ;
    
    cout << "Enter your age: " ;
    cin >> age ;
    cout << "Enter your monthly income: " ;
    cin >> income ;
    cout << "Enter your Credit Score: " ;
    cin >> credit ;
  
    if ((age >= 21 && age <= 60) && (income >= 25000) && (credit >= 700)) {
        cout << "Eligible" ;
    }    
    else if (age < 21 || age > 60) {
        cout << "Not Eligible. Age Condition Failed. " ;
    }
    else if (income < 25000) {
        cout << "Not Eligible. Income Condition Failed" ;
    }
    else if (credit < 700) {
        cout << "Not Eligible. Credit Score Condition Failed" ;
    }
   
    return 0;
}
