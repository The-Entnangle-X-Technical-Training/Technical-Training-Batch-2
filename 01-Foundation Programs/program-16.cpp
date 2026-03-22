// Write a program that takes a single alphabet character and checks if it is uppercase or lowercase. Display
// the result.


#include <iostream>
using namespace std;
int main() 
{
    char c;
    cout<<"Enter a single alphabet character : ";
    cin>>c;
    
    if((c >= 65 && c<= 90)) 
    {
        cout<<c<<" is Uppercase."; 
    }else if (c >= 97 && c <= 122)
    {
        cout<<c<<" is Lowercase";
    }else{
        cout<<c<<"invalid alphabet ";
    }
    
    

    return 0;
}