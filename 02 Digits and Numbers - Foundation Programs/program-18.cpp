// Write a program that takes a 3-digit number as input and checks if its digits are in strictly ascending order
// (e.g., 123 is yes, 132 is no).


#include<iostream>
using namespace std;
int main()
{
    int number,first_digit,second_digit,last_digit;
    cout<<"Enter 3-digit number : ";
    cin>>number;
    first_digit=number/100;
    second_digit=(number/10)%10;
    last_digit=number%10;
    if (first_digit<second_digit)
    {
        if (second_digit<last_digit)
        {
            cout<<number<<" is a ascending order.";
        }
        else{
            cout<<number<<" is not a ascending order.";
        }
        
    }else{
        cout<<number<<" is not a ascending order.";
    }
     
    return 0;
}