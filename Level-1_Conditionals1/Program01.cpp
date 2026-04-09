#include <iostream>
using namespace std;

int main()
{
    int num ;
    
    cout << "Enter a Number : " ;
    cin >> num ;
    
    if (num % 2 == 0 ) {
      cout << "This is an Even Number " ;
    }
    else 
    cout << " This is an Odd Number " ;

    return 0;
}
