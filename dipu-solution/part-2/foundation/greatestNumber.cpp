#include<iostream>
using namespace std;
int main (){
    int a, b, c;
    int greatest;

    cout << "Enter the first number = ";
    cin >> a;
    cout << "Enter the Second number = ";
    cin >> b;
    cout << "Enter the Third number = ";
    cin >> c;

    if (a >=b && a >=c)
    {
        greatest = a;
    }
    else if(b<= a && b<=c){
        greatest = b;
    }
    else{
        greatest = c;
    }

    cout << "The greatest digits of three number " << greatest << "";
}