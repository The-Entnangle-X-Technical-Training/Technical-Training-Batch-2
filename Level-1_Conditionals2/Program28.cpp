#include <iostream>
using namespace std;

int main()
{
    int num ;
    
    cout << "Enter a Number : " ;
    cin >> num ;
    
    if (num % 3 == 0) {
        cout << " The Number is Divisible by 3" ;
    }
    if (num % 5 == 0) {
        cout << " The Number is Divisible by 5" ;
    }
    if (num % 3 == 0 && num % 5 == 0) {
        cout << " The Number is Divisible by both 3 and 5 " ;
    }
    if (num % 3 != 0 && num % 5 != 0) {
        cout << " The Number is Divisible by none " ;
    }

    return 0;
}
