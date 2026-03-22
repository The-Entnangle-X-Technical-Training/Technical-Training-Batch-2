#include<iostream>
using namespace std;
int main(){
    int n;
    cout << "Enter the angle of triangle = ";
    cin >> n;

    if (n<90)
    {
        cout << "These Triangle is Acute angle ";
    }
    else if (n == 90)
    {
        cout << "These Triangle is Right angle ";
    }
    else if (n>90)
    {
        cout << "These Triangle is Obtuse angle ";
    }
    else{
        cout << "Invaild Triangle ";
    }
    
}