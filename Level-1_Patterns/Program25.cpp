#include <iostream>
using namespace std;

int main() 
{
  int N ;
    cout << "Enter an Odd No. ";
    cin >> N ;
    
    int mid = N / 2 + 1 ;
    
    for (int i =1; i<=N; i++) {
      for (int j =1; j<=N; j++) {
        if(i == mid || j == mid)
                cout << "*";
            else
                cout << " ";
      }
          cout << endl ;
    }
    return 0;
}
