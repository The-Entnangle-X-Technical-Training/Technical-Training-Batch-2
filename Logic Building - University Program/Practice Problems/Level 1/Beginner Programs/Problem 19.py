#Problem 19: Simple Interest with Total Amount

Principal = int(input("Enter principal amount: "))
Rate = int(input("Enter rate of interest: "))
Time = int(input("Enter time (in years): "))

Simple_Interest = (Principal * Rate * Time) / 100
Total_Amount = Simple_Interest + Principal

print("Simple Interest: ", Simple_Interest)
print("Total Amount: ", Total_Amount)

