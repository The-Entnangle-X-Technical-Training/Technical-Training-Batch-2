#include <iostream>
using namespace std;

int main() 
{
  int arr[6], reverse ;
  cout << "Enter 6 Numbers: " ;
  for (int i = 0; i < 6; i++) {
    cin >> arr[i] ;
  }
  cout << "Reverse of the Array = " ;
    for (int i = 5; i >= 0; i--) {
      reverse = arr[i] ;
      cout << reverse << endl;
      }
    
    return 0;
}
