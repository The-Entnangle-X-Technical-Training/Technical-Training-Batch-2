N = input("Enter a number : ")

try:
    N = int(N)
    fact = 1
    for i in range(1, N+1):
        fact *= i
    print(fact)
except ValueError:
    print("Enter a valid number")