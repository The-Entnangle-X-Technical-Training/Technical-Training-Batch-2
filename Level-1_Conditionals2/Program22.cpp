#include <iostream>
using namespace std;

int main()
{
    int month, year ;
    
    cout << "Enter the number of Month : " ;
    cin >> month ;
    cout << "Enter Year: " ;
    cin >> year ;
    
    if (month == 1) {
        cout << "Month- January. No. of days = 31 " ;
    } 
    else if (month == 2 && year % 4 == 0) {
      cout << " Month - February. No. of days in February in a Leap Year = 29 " ;
    }
    else if (month == 2 && year % 4 != 0) {
      cout << " Month - February. No. of days = 28 " ;
    }
    else if (month == 3) {
      cout << " Month - March. No. of days = 31 " ;
    }
    else if (month == 4) {
      cout << " Month - April. No. of days = 30 " ;
    }
     else if (month == 5) {
      cout << " Month - May. No. of days = 31 " ;
    }
     else if (month == 6) {
      cout << " Month - June. No. of days = 30 " ;
    }
     else if (month == 7) {
      cout << " Month - July. No. of days = 31 " ;
    }
     else if (month == 8) {
      cout << " Month - August. No. of days = 31 " ;
    }
     else if (month == 9) {
      cout << " Month - September. No. of days = 30 " ;
    }
     else if (month == 10) {
      cout << " Month - October. No. of days = 31 " ;
    }
     else if (month == 11) {
      cout << " Month - November. No. of days = 30 " ;
    }
     else if (month == 12) {
      cout << " Month - December. No. of days = 31 " ;
    }
    else {
      cout << " Enter a valid number " ;
    }

    return 0;
}
