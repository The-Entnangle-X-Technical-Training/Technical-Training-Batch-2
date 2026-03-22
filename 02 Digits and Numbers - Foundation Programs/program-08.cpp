// Write a program that takes a 3-digit number as input and swaps its first and last digits, then displays the
// result (e.g., 456 becomes 654).


#include<iostream>
using namespace std;
int main()
{
    int number,rev_digit;
    cout<<"Enter 3-digit number : ";
    cin>>number;
    
    rev_digit=(number%10)*100;  //123 as input number we got 3*100 = 300
    rev_digit=rev_digit+((number/10)%10)*10;
    rev_digit=rev_digit+(number/100);

    cout<<"reverse order : "<<rev_digit;

    return 0;
}