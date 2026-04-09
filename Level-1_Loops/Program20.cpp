#include <iostream>
using namespace std;

int main()
{
  int num, count= 0 ;
  cout << "Enter a Number: " ;
  cin >> num;
   if (num == 0)
     count = 1 ;
   if (num < 0)
     num = (- num) ;
   while (num > 0) {
     num = num / 10 ;
     count ++ ;
   }
   cout << "Total Number of Digits = " << count << endl ;
    return 0;
}
