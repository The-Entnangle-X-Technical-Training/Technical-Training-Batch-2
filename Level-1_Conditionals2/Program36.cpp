#include <iostream>
using namespace std;

int main()
{
    int length, upper, lower, digits ;
    int types = 0 ;
    
    cout << "Enter Password Length : " ;
    cin >> length ;
    cout << "Enter count of uppercase characters : " ;
    cin >> upper ;
    cout << "Enter count of lowercase characters : " ;
    cin >> lower ;
    cout << "Enter count of digits : " ;
    cin >> digits ;
  
    if (upper > 0)
        types++;

    if (lower > 0)
        types++;

    if (digits > 0)
        types++;
    
    if (length >= 8 && upper > 0 && lower > 0 && digits > 0)
        cout << "Strong Password";
    else if (length >= 6 && types >= 2)
        cout << "Medium Password";
    else
        cout << "Weak Password";
    
   
    return 0;
}
