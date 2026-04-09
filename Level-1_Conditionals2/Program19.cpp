#include <iostream>
using namespace std;

int main()
{
    double x, y ;
    
    cout << "Enter Two Co-ordinates " ;
    cin >> x >> y ;
    
    if (x > 0 && y > 0) {
        cout << " First Quandrant -> I " ;
    } 
    
    else if (x < 0 && y > 0) {
      cout << " Second Quandrant -> II " ;
    }
    
    else if (x < 0 && y < 0) {
      cout << " Third Quandrant -> III " ;
    }
    
    else if (x > 0 && y < 0) {
      cout << " Fourth Quandrant -> IV " ;
    }
    
    else if (x > 0 && y == 0) {
      cout << " Positive X-Axis " ;
    }
    
     else if (x < 0 && y == 0) {
      cout << " Negative X-Axis " ;
    }
    
     else if (x == 0 && y > 0) {
      cout << " Positive Y-Axis " ;
    }
    
     else if (x == 0 && y < 0) {
      cout << " Negative Y-Axis " ;
    }
    
    else {
      cout << " Origin " ;
    }

    return 0;
}
