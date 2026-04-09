#include <iostream>
using namespace std;

int main()
{
    double phy, chem, maths, bio, eng, total, avg ;
    
    cout << "Enter total marks out of 100 in Physics : " ;
    cin >> phy ;
    cout << "Enter total marks out of 100 in Chemistry : " ;
    cin >> chem ;
    cout << "Enter total marks out of 100 in Mathematics : " ;
    cin >> maths ;
    cout << "Enter total marks out of 100 in Biology : " ;
    cin >> bio ;
    cout << "Enter total marks out of 100 in English : " ;
    cin >> eng ;
    
    total = phy + chem + maths + bio + eng ;
    cout << " Total marks in 5 Subjects = " << total << endl ;
    
    avg = total / 5 ;
    cout << " Average marks in 5 Subjects = " << avg << endl ;

    return 0;
}
