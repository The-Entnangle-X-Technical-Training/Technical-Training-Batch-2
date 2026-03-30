#Write a program that takes an alphabet character (A-Z or a-z) and displays if it falls in first half (A-M) or second half (N-Z) of alphabets.
char=input("Enter an alphabet character: ")
if('A'<=char<='M' or 'a'<=char<='m'):
    print("First Half: A-M ")
elif('N'<=char<='Z' or 'n'<=char<='z'):
    print("Second Half: N-Z ")
else:
    print("Enter Correct Value")