#include <iostream>
using namespace std;

int main()
{
    int total_secs, secs, mins, hours ;
    cout << "Enter total seconds : ";
    cin >> total_secs ;
    hours = total_secs / 3600 ;
    total_secs = total_secs % 3600 ;
    mins = total_secs / 60 ;
    secs = total_secs % 60 ;

    cout << "Hours: " << hours << " Minutes:" << mins << " Seconds: " << secs << endl;

    return 0;
}
