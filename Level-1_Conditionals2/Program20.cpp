#include <iostream>
using namespace std;

int main()
{
    double bmi ;
    
    cout << "Enter your Body Mass Index (BMI): " ;
    cin >> bmi ;
    
    if (bmi< 18.5) {
        cout << " Underweight " ;
    } 
    
    else if (bmi >= 18.5 && bmi<= 24.9) {
      cout << " Normal " ;
    }
    
    else if (bmi >= 25 && bmi<= 29.9) {
      cout << " Overweight " ;
    }
    else {
      cout << " Obese " ;
    }

    return 0;
}
