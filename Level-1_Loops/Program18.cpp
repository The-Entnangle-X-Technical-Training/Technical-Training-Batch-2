#include <iostream>
using namespace std;

int main()
{
  int N ;
  long factorial = 1 ;
  cout << "Enter a Number:" ;
  cin >> N;
  cout << " Factorial of " << N << " =" << endl;
  
  for (int i =1; i <=N; i++) {
   factorial = factorial * i ;
}
 cout << factorial << endl ;
    return 0;
}
