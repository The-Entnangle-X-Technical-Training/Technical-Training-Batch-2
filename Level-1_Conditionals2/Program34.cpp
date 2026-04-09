#include <iostream>
using namespace std;

int main()
{
    double income, increment=0, newSalary ;
    int rating, years ;
    
    cout << "Enter your current salary " ;
    cin >> income ;
    cout << "Enter your performance rating " ;
    cin >> rating ;
    cout << "Enter years of service " ;
    cin >> years ;
  
    if (rating == 5)
        increment = income * 0.20;
    else if (rating == 4)
        increment = income * 0.15;
    else if (rating == 3)
        increment = income * 0.10;
    else if (rating == 2)
        increment = income * 0.05;
    else if (rating == 1)
        increment = 0;
    else {
      cout << "Invalid Rating";
    }
   if (years > 5)
        increment = increment + (income * 0.05);
  
   newSalary = income + increment ;
   
   cout << "New Salary: " << newSalary << endl;
   
    return 0;
}
