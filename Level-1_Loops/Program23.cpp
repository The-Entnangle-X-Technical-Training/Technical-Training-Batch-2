#include <iostream>
using namespace std;

int main()
{
  int num, i ;
  cout << "Enter a Number: " ;
  cin >> num;

  if (num <= 0) {
   cout << " This is not Prime Number " ;
   return 0 ;
  }
  for (i=2 ; i < num ; i++) {
    if (num % i == 0) {
      cout << "This is not a Prime Number " ;
      return 0 ;
    }
  }  
    cout << "This is a Prime Number " ;
    
    return 0;
}
