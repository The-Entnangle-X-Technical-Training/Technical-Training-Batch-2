#include <iostream>
using namespace std;

int main()
{
  int N, count =0 ;
  cout << "Number of Even No. between 1 to " << N << ":" << endl;
  cin >> N;
  for (int i =1; i <=N; i++) {
   if( i % 2 == 0) 
   count ++ ;
}
 cout << count << endl ;
    return 0;
}
