#include <iostream>
using namespace std;

int main()
{
  int N, count = 0 ;
  cout << "Enter a Number: " ;
  cin >> N ;
  
  cout << " Numbers divisible by 3 from 1 to N = " ;
  for (int i = 1; i <= N; i++) {
    if (i % 3 == 0) {
      count ++ ;
    }
  }
  cout << count << endl ;
    return 0;
}
