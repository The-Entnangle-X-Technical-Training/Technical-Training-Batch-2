print('Enter one character to chek(vowel/constent):',end="")
num1=input()
if(num1>= "a"  and num1<= "z" ):
    print("This is Lower Case Letter:")
elif(num1>= "A" and num1<="Z"): 
   print("This is Upper Case Letter:")
else:
    print("This is not a Character:")