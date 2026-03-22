#include<iostream>
using namespace std;
int main (){
    int a, b, c;
    int smallest;

    cout << "Enter the first number = ";
    cin >> a;
    cout << "Enter the Second number = ";
    cin >> b;
    cout << "Enter the Third number = ";
    cin >> c;

    if (a <=b && a <=c)
    {
        smallest = a;
    }
    else if(b<= a && b<=c){
        smallest = b;
    }
    else{
        smallest = c;
    }

    cout << "The smallest digits of three number " << smallest << "";
}