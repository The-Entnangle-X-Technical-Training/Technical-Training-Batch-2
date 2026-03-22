// Write a program that takes a 4-digit number as input and finds the smallest digit in it, then displays that
// digit.


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

    if (first_digit<second_digit)
    {
        if (first_digit<third_digit)
        {
            if (first_digit<last_digit)
            {
                cout<<first_digit<<" is smallest digit.";
            }
            else{
                cout<<last_digit<<" is smallest digit.";
            }
            
        }else if (third_digit<last_digit)
        {
            cout<<third_digit<<" is smallest digit.";
        }else{
            cout<<last_digit<<" is smallest digit.";

        }
        
    }else if (second_digit<third_digit)
    {
        if (second_digit<last_digit)
        {
            cout<<second_digit<<" is smallest digit.";
        }else{
            cout<<last_digit<<" is smallest digit.";
        }
        
    }else if (third_digit<last_digit)
    {
        cout<<third_digit<<" is smallest digit.";
    }else{
        cout<<last_digit<<" is smallest digit.";
    }
    
    return 0;
}