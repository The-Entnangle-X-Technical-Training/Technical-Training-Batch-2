#include <iostream>
using namespace std;

int main()
{
    int marks ;
    
    cout << "Enter your marks out of 100 : " ;
    cin >> marks ;
    if (marks > 100) {
      cout << "Enter marks out of 100 : " ;
    }
    
    if ( 100 >= marks >= 40 ) {
      cout << " Pass " ;
    }
    
    else 
    cout << " Fail " ;

    return 0;
}
