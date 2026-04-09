#include <iostream>
using namespace std;

int main()
{
  int base, exponent ;
  long result = 1 ;
  cout << "Enter Base : " ;
  cin >> base ;
  cout << "Enter Exponent : " ;
  cin >> exponent ;
  
  for (int i = 1; i <= exponent; i++) {
    result = result * base ;
  }
  
  cout << " Result = " << result << endl ;
    return 0;
}
