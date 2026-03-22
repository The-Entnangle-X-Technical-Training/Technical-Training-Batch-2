// Write a program that takes the side of a square as input and calculates both its area and perimeter, then
// displays both results.
#include<iostream>
using namespace std;
int main ()
{
    int side_of_square;
    cout<<"Enter the side of the square: ";
    cin>>side_of_square;
    int area= side_of_square*side_of_square;   //area=side*side;
    int perimeter= 4*side_of_square;            //p=4*side;
    cout<<"area of square is : "<<area<<endl;
    cout<<"perimeter of square is : "<<perimeter<<endl;
    return 0;
}