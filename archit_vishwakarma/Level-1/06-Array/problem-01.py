list = []

i = 1
while i<=5:
    try:
        user = int(input("Enter number : "))
        list.append(user)
        i += 1
    except ValueError:
        print("Enter integer value")

print(list)