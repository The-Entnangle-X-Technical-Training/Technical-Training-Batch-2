#include <iostream>
using namespace std;

int main() 
{
  int M, N ;
  cout << "Enter no. of rows " ;
  cin >> M;
  cout << "Enter a no. " ;
  cin>> N ;
  for (int i=1; i<=M; i++) {
    for (int j=1; j<=N; j++) {
      cout << j ;
    }
    cout << endl ;
  }

    return 0;
}
