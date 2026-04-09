#include <iostream>
using namespace std;

int main()
{
    int num1, num2 ;
    
    cout << "Enter First Number : " ;
    cin >> num1 ;
    cout << "Enter Second Number : " ;
    cin >> num2 ;
    
    if (num1 > num2 ) {
      cout << "First Number is Greater than the Second Number " ;
    }
    else 
    cout << " Second Number is Greater than the First Number " ;

    return 0;
}
