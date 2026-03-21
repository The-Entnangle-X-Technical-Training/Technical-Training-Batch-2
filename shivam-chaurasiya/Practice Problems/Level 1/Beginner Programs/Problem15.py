# Swap Two Numbers Without Third Variable

a = int(input('Enter first number:'))   # 10
b = int(input('Enter second number:'))  # 20

print(f'Before Swapping the value of a and b is {a} and {b}')

def new_func(a, b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

a, b = new_func(a, b)

print(f'After Swapping the value of a and b is {a} and {b}')
