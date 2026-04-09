#include <iostream>
using namespace std;

int main()
{
    double marks ;
    
    cout << "Enter your marks out of 100 : " ;
    cin >> marks ;
    
    if (marks >= 40 && marks <= 100) {
        cout << " Pass " ;
    } 
    
    else if (marks < 40) {
      cout << " Fail " ;
    }
    
    else {
    cout << " Enter valid marks out of 100 " ;
    }

    return 0;
}
