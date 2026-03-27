#include <stdio.h>

int main(){

    float price;
    float discount;
    printf("Enter Price : ");
    scanf("%f", &price);

    printf("Enter Discount percentage number:");
    scanf("%f", &discount);

    float discount_amt = price*(discount/100);
    float final_price = price - discount_amt;
    printf("Discount of: %.2f\n", discount_amt);
    printf("Final Price: %.2f\n", final_price);
    return 0;
}