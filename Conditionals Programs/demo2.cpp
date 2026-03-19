#include<iostream>
using namespace std;

int main(){

   int numberOne = 0;

   cout<<"Enter a number: ";
   cin>>numberOne;

   if(0<numberOne){ // 0 < 5
    cout<<"Positve Number"<<endl;
   }

  else if(numberOne<0){
    cout<<"Negative Number"<<endl;
   }

   else{
    cout<<"Zero"<<endl;
   }

}