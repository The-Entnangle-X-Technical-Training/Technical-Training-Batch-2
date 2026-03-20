#include <iostream>
using namespace std;
int main() {
    // Write C++ code here
    int pamount, rate, time;
    int si;
    cout<<"Enter Principal Amount : ";
    cin>>pamount;
    cout<<"Enter rate of interest : ";
    cin>>rate;
    cout<<"Enter Time Period : ";
    cin>>time;
    si=(pamount*rate*time)/100;
    cout<<"Simple Interest : "<<si<<endl;
    cout<<"Total amount : "<<si+pamount<<endl;

    return 0;
}