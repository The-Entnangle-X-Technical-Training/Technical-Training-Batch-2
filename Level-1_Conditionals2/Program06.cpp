#include <iostream>
using namespace std;

int main()
{
    char ch ;
    
    cout << "Enter a Single Character : " ;
    cin >> ch ;
    
    if ((ch >= 65 && ch <= 90) || (ch >= 97 && ch <= 122)) {
        cout << " This is an Alphabet ->" << ch << endl;
    } 
    
    else if (ch >= 48 && ch <= 57) {
      cout << " This is a digit -> " << ch << endl ;
    }
    
    else {
    cout << " This is a special character -> " << ch << endl ;
    }

    return 0;
}
