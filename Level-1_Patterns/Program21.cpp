#include <iostream>
using namespace std;

int main() 
{
  int N ;
    cout << "Enter no. of rows ";
    cin >> N ;
    
    for (int i =N; i>=1; i--) {
      for (int j =1; j<=i; j++) {
          cout << j ;
      }
          cout << endl;
  
    }
    return 0;
}
