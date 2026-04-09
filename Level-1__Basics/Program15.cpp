#include <iostream>
using namespace std;

int main() 
{
    int num1, num2, swap ;
    cout << " Enter First Number : " ;
    cin >> num1 ;
    cout << " Enter the Second Number : " ;
    cin >> num2 ;
    cout << " Before Swapping : " << endl ;
    cout << " num1 = " << num1 << " , num2 = " << num2 << endl ;
    num1 = num1 + num2 ;
    num2 = num1 - num2 ;
    num1 = num1 - num2 ;
    cout << " After Swapping : " << endl ;
    cout << " num1 = " << num1 << " , num2 = " << num2 << endl ;
    return 0;
}
