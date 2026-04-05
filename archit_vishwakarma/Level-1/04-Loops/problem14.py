N = input("Enter a number : ")

count = 0
if N.isdigit():
    N = int(N)
    for i in range(2, N+1, +2):
        count += 1
    print(count)
else:
    print("Enter a valid number")
