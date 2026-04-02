char = input("Enter a single alphabate : ")

if len(char)==1 and char.isalpha():
    if char == char.lower():
        print("Lowercase")
    else:
        print("Upper case")
else:
    print("Please enter a single al;phabate chracter")