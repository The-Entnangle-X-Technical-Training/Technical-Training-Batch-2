#include <iostream>
using namespace std;

int main()
{
    int num ;
    
    cout << "Enter a Number : " ;
    cin >> num ;
    if (num % 10 == 0) {
      cout << " Divisible by 10 " ;
    }
    
    else 
    cout << " Not Divisible by 10 " ;

    return 0;
}
