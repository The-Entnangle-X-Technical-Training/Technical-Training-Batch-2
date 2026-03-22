// Write a program that converts total seconds into hours, minutes, and seconds format and displays the
// result
#include<iostream>
using namespace std;
int main()
{
    int seconds,hours,minutes,remianing_seconds;;
    cout<<"Enter total seconds : ";
    cin>>seconds;

    hours=seconds/3600;
    remianing_seconds=seconds%3600;
    minutes=remianing_seconds/60;
    remianing_seconds=remianing_seconds%60;

    cout<<hours<<"-Hours,"<<minutes<<"-minutes,"<<remianing_seconds<<"-Seconds"<<endl;
    cout<<hours<<" :"<<minutes<<" :"<<remianing_seconds<<endl;

    return 0;
}