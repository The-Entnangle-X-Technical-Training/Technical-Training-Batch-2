// Write a program that takes three angles of a triangle and displays whether it is Acute (all angles < 90°),
// Right (one angle = 90°), or Obtuse (one angle > 90°) triangle

#include <iostream>
using namespace std;
int main() {

    int a,b,c;

    cout<<"Enter First angle : ";
    cin>>a;
    cout<<"Enter Second angle : ";
    cin>>b;
    cout<<"Enter third angle : ";
    cin>>c;
    
    // according to condition;
     if (a < 90 && b < 90 && c < 90) {
            cout<<"Acute Triangle";
    }
    else if (a == 90 || b == 90 || c == 90) {
            cout<<"Right Triangle";
    }
    else if ( a > 90 || b > 90 || c > 90)
    {
            cout<<"Obtuse Triangle";
    }
   
    return 0;
}