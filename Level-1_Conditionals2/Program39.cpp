#include <iostream>
using namespace std;

int main()
{
    float weight, distance;
    float cost = 50;   

    cout << "Enter weight (kg): ";
    cin >> weight;

    cout << "Enter distance (km): ";
    cin >> distance;

    if (weight > 5)
        cost = cost + (weight * 10);

    if (distance > 100)
        cost = cost + (distance * 5);

    if (weight > 5 && distance > 100)
        cost = cost + 20;
    
    cout << "Total Shipping Cost = Rs. " << cost << endl;

    return 0;
}
