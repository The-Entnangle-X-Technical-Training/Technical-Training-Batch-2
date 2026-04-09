#include <iostream>
using namespace std;

int main() 
{
  int arr[6] ;
  cout << "Enter 6 Numbers" ;
  for (int i = 0; i < 6; i++) {
    cin >> arr[i] ;
  }
    int largest = arr[0] ;
    for (int i = 1; i < 6; i++) {
      if (arr[i] > largest) {
        largest = arr[i] ;
      }
    }
    cout << "Largest element of the Array = " << largest << endl;
    return 0;
}
