#include <iostream>
using namespace std;

int main() 
{
  int N, count=0 ;
  cout << "Enter no. of rows: " ;
  cin >> N ;
  
    for (int i=1; i <= N; i ++) {
      for (int j= 1; j <= i; j ++) {
        cout << j ;
      }
      cout << endl ;
    }
    return 0;
}
