N = input("Enter a number : ")

try:
    N = int(N)
    for i in range(3, N+1, +3):
        print(i)
except ValueError:
    print("Enter a valid number")