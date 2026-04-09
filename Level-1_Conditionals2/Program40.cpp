#include <iostream>
using namespace std;

int main()
{
    float usage, bill;

    cout << "Enter water usage (in Litres): ";
    cin >> usage;
    
    if (usage <= 5000)
        bill = usage * 2;
    else if (usage <= 10000)
        bill = usage * 3;
    else
        bill = usage * 5;
        
    if (usage < 3000)
        bill = bill - (bill * 0.15);

    cout << "Total Water Bill = Rs. " << bill << endl;


    return 0;
}
