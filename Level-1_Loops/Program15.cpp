#include <iostream>
using namespace std;

int main()
{
  int N, count =0 ;
  cout << "Enter a Number:" ;
  cin >> N;
  cout << "Number of Odd No. between 1 to " << N << ":" << endl;
  
  for (int i =1; i <=N; i++) {
   if( i % 2 != 0) 
   count ++ ;
}
 cout << count << endl ;
    return 0;
}
