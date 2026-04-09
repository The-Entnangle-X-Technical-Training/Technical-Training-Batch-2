#include <iostream>
using namespace std;

int main()
{
    double weight, height, bmi ;
    
    cout << "Enter the Weight in Kilograms : " ;
    cin >> weight ;
    cout << "Enter the Height in Meters : " ;
    cin >> height ;
    
    bmi = weight / (height * height) ;
    cout << " Body Mass Index : " << bmi << endl ;

    return 0;
}
