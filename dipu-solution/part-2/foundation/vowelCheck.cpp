#include<iostream>
using namespace std;
int main(){
    char vow;
    cout << "Enter the character for check which character is vowerl and consonat = ";
    cin >> vow;

    if (vow == 'a'|| vow == 'e'|| vow == 'i'|| vow == 'o'|| vow == 'u'|| vow == 'A'|| vow == 'E'|| vow == 'I'|| vow == 'O'|| vow == 'U' )
    {
        cout << " These character Letter is vowel " << vow << "";
    }
    else{
        cout<< " These character Letter is consonant " << vow << "";
    }
    
}