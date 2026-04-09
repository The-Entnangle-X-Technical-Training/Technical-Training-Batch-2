#include <iostream>
using namespace std;

int main()
{
    int day, month ;
    
    cout << "Enter a Day of the Month (1-31) : " ;
    cin >> day ;
    cout << "Enter a Month (1-12) : " ;
    cin >> month ;
    if ((day >=1 && day<= 31) && month == 1 || month == 3 || 
    month == 5 || month ==7 || month ==8 || month ==10 || month ==12){
        cout << " Valid " ;
    }
    else if ((day >=1 && day <=29) && month ==2) {
        cout << " Valid " ;
    }
    else if ((day >=1 && day<= 30) && month ==4 || month == 6 ||
    month == 9 || month ==11) {
        cout << " Valid " ;
    }
    else {
        cout << " Invalid Date " ;
    }

    return 0;
}
