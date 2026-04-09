#include <iostream>
using namespace std;

int main() 
{
  int N ;
  cout << "Enter no. of rows: " ;
  cin >> N ;
  
    for (int i=1; i<=N; i++) {
      for (int j=1; j <= 4; j++) {
        cout << i << " " ;
      }
      cout << endl;
    }
    return 0;
}
