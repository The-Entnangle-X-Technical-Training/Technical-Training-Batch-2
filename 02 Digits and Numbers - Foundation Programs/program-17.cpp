// write a program that takes a 4-digit number as input and counts how many of its digits are even, then
// displays the count.


#include<iostream>
using namespace std;
int main()
{
    int number,first_digit,second_digit,third_digit,last_digit,even_counter;
    cout<<"Enter 4-digit number : ";
    cin>>number;
    first_digit=number/1000;
    second_digit=(number/100)%10;
    third_digit=(number/10)%10;
    last_digit=number%10;

    even_counter=0;
    if (first_digit%2==0)
    {
        even_counter++;
    }
    if (second_digit%2==0)
    {
        even_counter++;
    }if (third_digit%2==0)
    {
        even_counter++;
    }if (last_digit%2==0)
    {
        even_counter++;
    }

    cout<<even_counter<<" digit are even.";
    


    return 0;
}