#include <iostream>
using namespace std;

int main()
{
  int N, sum=0 ;
  cout << "Enter a Number: ";
  cin >> N ;
  for (int i =1; i <=N; i++) {
  sum = sum+i ;
}
  cout<< "Sum of Numbers from 1-N: " << sum << endl;
    return 0;
}
