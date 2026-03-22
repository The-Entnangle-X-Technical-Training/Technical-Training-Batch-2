// Write a program that takes any number as input and checks whether its last digit is even or odd, then
// displays the result


#include<iostream>
using namespace std;
int main()
{
    int number,last_digit;
    cout<<"Enter any number : ";
    cin>>number;

    last_digit=number%10;    //store last digit
    if (last_digit%2==0)     // check it is divisble by 2 or not
    {
        cout<<"The Last digit is even.";
    }else{
        cout<<"The Last digit is odd.";
    }

    return 0;
}