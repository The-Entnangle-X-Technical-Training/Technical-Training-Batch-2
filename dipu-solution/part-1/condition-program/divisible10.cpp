#include<iostream>
using namespace std;
int main(){
    int num;
    cout << "Enter the number ";
    cin >> num;

    if (num%10 == 0)
    {
        cout << "These number is divisible by 10 ";
    }
    else{
        cout << "These number is not divisible by  10";
    }
}