N = input("Enter a number : ")

if N.isdigit():
    N = int(N)
    for i in range(1, 10+1):
        print(f"{N} x {i} = {N*i}")
else:
    print("Enter a valid number")