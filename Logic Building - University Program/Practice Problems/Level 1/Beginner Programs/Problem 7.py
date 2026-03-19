#Problem 7: Simple Interest Calculatior

Principal = int(input("Enter principal amount: "))
Rate = int(input("Enter rate of interest: "))
Time = int(input("Enter time (in years): "))

Simple_Interest = (Principal * Rate * Time) / 100

print("Simple Interest: ", Simple_Interest)