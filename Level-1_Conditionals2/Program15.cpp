#include <iostream>
using namespace std;

int main()
{
    int num ;
    
    cout << "Enter a Number: " ;
    cin >> num ;
    
    if (num >= 0 && num <= 9) {
        cout << " This is a Single Digit Number -> " << num << endl ;
    } 
    
    else if (num >=10 && num <=99) {
        cout << " This is a Double Digit Number -> " << num << endl ;
    }
    
    else {
      cout << " This Number is more than Double Digit -> " << num << endl ;
    }

    return 0;
}
