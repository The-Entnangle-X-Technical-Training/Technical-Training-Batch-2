#include <iostream>
using namespace std;

int main()
{
    char letter ;
    
    cout << "Enter an Alphabet (Capital or Small) : " ;
    cin >> letter ;
    
    if (letter >= 65 && letter <= 77 || letter >=97 && letter <=109) {
        cout << " First Half " ;
    }
     else if (letter >= 78 && letter <= 90 || letter >= 110 && letter <= 122) {
      cout << " Second Half " ;
    }
    else {
      cout << " Enter a valid character " ;
    }

    return 0;
}
