// Write a program that takes total number of days as input and converts it into years, weeks, and remaining
// days, then displays all three values
#include<iostream>
using namespace std;
int main()
{
    int days;
    cout<<"Enter total number of days : ";
    cin>>days;
    int years,weeks,remaining_days;

    years=days/365;
    remaining_days=days%365;
    weeks=remaining_days/7;
    remaining_days=remaining_days%7;
    
    cout<<"Year : "<<years<<endl;
    cout<<"Weeks : "<<weeks<<endl;
    cout<<"remaining days : "<<remaining_days;
    return 0;
    
}
