#include <iostream>
using namespace std;

int main() 
{
    int number = 10;
    std::cout << "Initial value: " << number << std::endl;
    number = 20;
    std::cout << "Value after updating to 20: " << number << std::endl;
    number = 20 + 5;
    std::cout << "Value after adding 5: " << number << std::endl;
    number = number * 2;
    std::cout << "Value after multiplying by 2: " << number << std::endl;
    return 0;
}
