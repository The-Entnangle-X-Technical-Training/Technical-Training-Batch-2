#include <iostream>
using namespace std;

int main() 
{
  char letter ;
    cout << " Enter an alphabet: ";
    cin >> letter ;
    
    if (!isalpha(letter)) {
      cout << " Not an alphabet ";
    }
    else if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o'
    || letter == 'u' ||letter == 'A' || letter == 'E' || letter == 'I' || letter == 'O'
    || letter == 'U') {
      
    cout << " Vowel " ;
    }
    else {
      cout << " Consonent " ;
    }
    return 0 ;
}
