#include<iostream>
using namespace std;
int main(){
    char ch;
    cout << "Enter the alphabet character ";
    cin >> ch;

    if ((ch >= 'A' && ch <= 'Z'))
    {
        cout << "The character '" << ch << "' is upper case";
    }
    else if(ch>='a'&& ch<='z'){
        cout<< "The character '" << ch << "' is lower case";
    }
    else{
        cout << "invalid character ";
    }
}