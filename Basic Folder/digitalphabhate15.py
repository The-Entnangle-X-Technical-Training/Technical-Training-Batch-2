print('Enter one character to chek(vowel/constent):',end="")
num1=input()
if(num1>= "a"  and num1<= "z" ):
    print("This is Letter:")
elif(num1>= "A" and num1<="Z"): 
   print("This is Letter:")
elif(num1>='0'and num1<='9'):
    print("This is Number:")
else:
    print("This is Special Character:")