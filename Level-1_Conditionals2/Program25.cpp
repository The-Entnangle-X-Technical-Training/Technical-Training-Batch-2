#include <iostream>
using namespace std;

int main()
{
    int num ;
    
    cout << "Enter a Number : " ;
    cin >> num ;
    
    if (num>=1 && num <= 10) {
        cout << " The Number lies in the range 1-10 " ;
    }
    else if (num>=11 && num <= 50) {
        cout << " The Number lies in the range 11-50 " ;
    }
    else if (num>=51 && num <= 100) {
        cout << " The Number lies in the range 51-100 " ;
    }
    else if (num>=101 && num <= 500) {
        cout << " The Number lies in the range 101-500 " ;
    }
    else if (num>=501 && num <= 1000) {
        cout << " The Number lies in the range 501-1000 " ;
    }
    else {
        cout << " The Number is greater than 1000 " ;
    }

    return 0;
}
