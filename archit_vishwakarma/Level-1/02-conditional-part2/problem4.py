dividend = int(input("Enter dividend : "))
divisor = int(input("Enter divisor : "))

if divisor == 0:
    print("Division by zero is not allowed")
else:
    print("Divisible" if dividend % divisor == 0 else "Not divisible")
    