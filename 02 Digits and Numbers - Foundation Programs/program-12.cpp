// Write a program that takes a 2-digit number as input and checks if it is a palindrome (reads same forwards
// and backwards). Example: 11 → Yes, 23 → No. Display "Palindrome" or "Not Palindrome"


#include<iostream>
using namespace std;
int main()
{
    int number,rev_digit;
    cout<<"Enter 2-digit number : ";
    cin>>number;


    rev_digit=(number%10)*10;
    rev_digit=rev_digit+(number/10);  //first we reverse the digit
    if (rev_digit==number)     //check both are equal or not
    {
        cout<<"Palindrome.";
    }else{
        cout<<"Not Palindrome.";
    }

    return 0;
}