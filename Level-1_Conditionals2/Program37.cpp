#include <iostream>
using namespace std;

int main()
{
    int maths, phy, chem, total ;
    
    cout << "Enter Marks in Mathematics out of 100 : " ;
    cin >> maths ;
    cout << "Enter Marks in Physics out of 100 : " ;
    cin >> phy ;
    cout << "Enter Marks in Chemistry out of 100 : " ;
    cin >> chem ;
    
    total = phy + maths + chem ;
    
    if (maths >= 80 && phy >= 75 && chem >= 75 || total >= 240) {
       cout << "Eligible" ;
    }   
    else {
        cout << "Not Eligible" ;
    }
   
    return 0;
}
