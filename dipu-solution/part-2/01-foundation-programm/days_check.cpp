#include<iostream>
using namespace std;
int main(){
    int totalDays, year, week, days, reaining;

    cout << "Enter the total Day of nummber = ";
    cin >> totalDays;

    year = totalDays / 365;

    reaining = totalDays % 365;

    week = reaining / 7;

    days = week % 7;

    cout << "years = " << year << endl;
    cout << "week = " <<week << endl;
    cout << "days = " << days << endl;
}