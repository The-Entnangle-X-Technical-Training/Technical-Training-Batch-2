#include <iostream>
using namespace std;

int main() 
{
    int maths, phy, chem, total, percent ;
    cout << "Enter total marks in Physics: " ;
    cin >> phy ;
    cout << "Enter total marks in Chemistry : " ;
    cin >> chem ;
    cout << "Enter total marks in Mathematics : " ;
    cin >> maths ;
    total = phy + chem + maths ;
    cout << "Your total marks out of 300 = " << total << endl ;
    percent = total / 3 ;
    cout << " Your total percentage = " << percent << endl ;
    return 0;
}
