#include <iostream>
using namespace std;

int main()
{
    double num1, num2, num3 ;
    
    cout << "Enter First Number: " ;
    cin >> num1 ;
    cout << "Enter Second Number: " ;
    cin >> num2 ;
    cout << "Enter Third Number: " ;
    cin >> num3 ;
    
    if (num1 < num2 && num1 < num3) {
        cout << " First number is the Smallest -> " << num1 << endl ;
    } 
    
    else if (num2 < num1 && num2 < num3) {
        cout << " Second number is the Smallest -> " << num2 << endl ;
    }
    
    else {
      cout << " Third Number is the Smallest -> " << num3 << endl ;
    }

    return 0;
}
