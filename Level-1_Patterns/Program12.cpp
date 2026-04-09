#include <iostream>
using namespace std;

int main() 
{
  int N, num ;
  cout << "Enter no. of rows: " ;
  cin >> N ;
  
    for (int i=1; i<=N; i++) {
      for (int j=i; j >= 1; j--) {
        cout <<  j << " " ;
      }
      cout << endl;
    }
    return 0;
}
