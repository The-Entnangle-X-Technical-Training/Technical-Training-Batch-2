#include <iostream>
using namespace std;

int main()
{
    float purchase, discount = 0, total;
    char member;

    cout << "Enter Purchase Amount: ";
    cin >> purchase;

    cout << "Are you a member? (Y/N): ";
    cin >> member;
    
    if (purchase > 10000)
        discount = purchase * 0.20;
    else if (purchase > 5000)
        discount = purchase * 0.15;
    else if (purchase > 2000)
        discount = purchase * 0.10;
        
    if (member == 'Y' || member == 'y')
        discount = discount + (purchase * 0.05);
    total = purchase - discount;

    cout << "Final Amount after Discount = " << total << endl ;
   
    return 0;
}
