#include <iostream>
using namespace std;

int main() 
{
  int arr[6] ;
  cout << "Enter 6 Numbers: " ;
  for (int i = 0; i < 6; i++) {
    cin >> arr[i] ;
  }
    int smallest = arr[0] ;
    for (int i = 1; i < 6; i++) {
      if (arr[i] < smallest) {
        smallest = arr[i] ;
      }
    }
    cout << "Smallest element of the Array = " << smallest << endl;
    return 0;
}
