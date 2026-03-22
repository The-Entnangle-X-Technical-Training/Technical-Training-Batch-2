// Write a program that takes a single character as input and checks if it is an alphabet (A-Z, a-z), digit (0-9),
// or special character. Display the result

#include <iostream>
using namespace std;
int main() 
{
    char c;
    cout<<"Enter a single character : ";
    cin>>c;
    char input_char;

    // if ((c>='a' && c=<'z') || (c=>'A' && c<='Z'))  // we got erro so i try to compare assic code
    if((c >= 65 && c<= 90) || (c >= 97 && c <= 122)) 
    {
        cout<<c<<" is an alphabet."; 
    }else if (c >= 45 && c <= 57)
    {
        cout<<c<<" is a digit.";
    }else{
        cout<<c<<" is a special character. ";
    }
    
    

    return 0;
}