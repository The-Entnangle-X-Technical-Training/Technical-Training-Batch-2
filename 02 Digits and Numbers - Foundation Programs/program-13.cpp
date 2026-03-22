// Write a program that takes a 3-digit number as input and checks if it is a palindrome. Example: 121 →
// Yes, 123 → No. Display "Palindrome" or "Not Palindrome"


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
    if (rev_digit==number)
    {
        cout<<"Palindrome.";
    }else{
        cout<<"Not Palindrome.";
    }
    
    return 0;
}