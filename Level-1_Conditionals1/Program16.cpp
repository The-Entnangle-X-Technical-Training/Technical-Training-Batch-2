#include <iostream>
using namespace std;

int main() 
{
  int marks ;
    cout << " Enter marks out of 100 : ";
    cin >> marks ;
    
    if (marks > 100 )
    cout << " Invalid marks " ;
    else if (marks >= 90)
    cout << " A " ;
    else if (marks >= 70)
    cout << " B " ;
    else if (marks >= 40)
    cout << " C " ;
    else 
    cout << "Fail" ;
    return 0 ;
}
