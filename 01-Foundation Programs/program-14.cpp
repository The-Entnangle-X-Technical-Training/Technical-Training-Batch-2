// Write a program that takes a single character as input and checks if it is a vowel (a, e, i, o, u, A, E, I, O,
// U) or consonant. Display the result
#include <iostream>
using namespace std;
int main() {
    char c;
    cout<<"Enter a single character : ";
    cin>>c;

    if (c=='a'||c=='A'||c=='e'||c=='E'||c=='i'||c=='I'||c=='o'||c=='O'||c=='u'||c=='U')
    {
        cout<<c<<" is a vowel.";
    }else{
        cout<<c<<" is a consonant.";
    }
    


    return 0;
}