// Write a program that takes a 4-digit number ABCD and checks if it contains the digit 0 anywhere except
// the first position. Example: 4012 → Duck Number, 0123 → Not Duck, 1234 → Not Duck. Display
// "Duck Number" or "Not Duck Number"


#include<iostream>
using namespace std;
int main()
{
    int number,first_digit,second_digit,third_digit,last_digit;
    cout<<"Enter 4-digit number : ";
    cin>>number;
    first_digit=number/1000;
    second_digit=(number/100)%10;
    third_digit=(number/10)%10;
    last_digit=number%10;

    if (first_digit==0)
    {
        cout<<"Not Duck Number.";
    }else if (second_digit==0||third_digit==0||last_digit==0)
    {
        cout<<"Duck Number.";
    } else    {
        cout<<"Not Duck Number.";
    }
    

    return 0;
}