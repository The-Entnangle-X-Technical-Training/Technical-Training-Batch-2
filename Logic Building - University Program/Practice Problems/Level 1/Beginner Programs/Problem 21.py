#Problem 21: Discount Price Calculator

Original_Price = float(input("Enter the original price: "))
Discount = float(input("Enter Discount (In Percentage): "))

Final_Price = (Original_Price * Discount) / 100

print("The final price after discount: ", Final_Price)