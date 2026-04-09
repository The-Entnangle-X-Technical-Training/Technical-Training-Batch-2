#include <iostream>
using namespace std;

int main()
{
  int N, sum = 0 ;
  cout << "Enter a Number:" ;
  cin >> N;
  cout << "Sum of Odd Numbers from 1 to " << N << ":" << endl;
  
  for (int i =1; i <=N; i++) {
   if( i % 2 != 0) 
   sum = sum + i ;
}
 cout << sum << endl ;
    return 0;
}
