#include <iostream>
using namespace std;

int main() 
{
  int arr[5] ;
    cout << "Enter 5 numbers: ";
    for (int i=0; i <5; i++) {
      cin >> arr[i] ;
    }
    cout << "Array Elements with Index:" ;
    for (int i =0; i<5; i++) {
      cout << "Index " << i << "-> " << arr [i] << " ";
    }
    return 0;
}
