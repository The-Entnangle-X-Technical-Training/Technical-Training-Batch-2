#include <iostream>
using namespace std;

int main()
{
  int N ;
  cout << "Enter a Number: " ;
  cin >> N ;
  cout << "First 10 Even Numbers : " ;
  for (int i =1; i <=N; i++) {
    if (i % 2!= 0)
    cout << i << endl;
}

    return 0;
}
