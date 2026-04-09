#include <iostream>
using namespace std;

int main()
{
    char ch ;
    
    cout << "Enter a Single Character : " ;
    cin >> ch ;
    
    if (ch >= 65 && ch <= 90) {
        cout << " Uppercase ->" << ch << endl;
    } 
    
    else if (ch >= 97 && ch <= 122) {
      cout << " Lowercase -> " << ch << endl ;
    }
    
    else {
    cout << " Enter a valid character -> " << ch << endl ;
    }

    return 0;
}
