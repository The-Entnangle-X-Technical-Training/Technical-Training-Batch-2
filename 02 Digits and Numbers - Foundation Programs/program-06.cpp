// Write a program that takes a 2-digit number as input and displays it in reverse order (e.g., 45 becomes
// 54).

#include<iostream>
using namespace std;
int main()
{
    int number,rev_digit;
    cout<<"Enter 2-digit number : ";
    cin>>number;
    
    rev_digit=(number%10)*10;
    rev_digit=rev_digit+(number/10);

    cout<<"reverse order : "<<rev_digit;

    return 0;
}