#include<iostream>
using namespace std;
int main(){
    int year;
    cout << "Enter the year for check leap or not leap = ";
    cin >> year;
    if((year%4==0 && year %100 != 0) || (year % 400 == 0)){
        cout << "These is a leap year = "<< year << endl;
    }
    else{
        cout << "These year is not a leap year = " << year << endl;
}
}