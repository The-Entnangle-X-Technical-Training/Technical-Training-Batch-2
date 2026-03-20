#include<iostream>
using namespace std;
int main(){
    int totalSecond, minutes, hours, seconds;
    cout << "Enter the total second = ";
    cin >> totalSecond;

    hours = totalSecond / 3600;
    int remaining = totalSecond % 3600;
    minutes = remaining / 60;
    seconds = totalSecond %60;

    cout << "Time = " << hours << endl;
    cout << "minutes = " << minutes << endl;
    cout << "seconds = " <<seconds << endl;

}