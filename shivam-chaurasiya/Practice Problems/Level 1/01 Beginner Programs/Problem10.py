# Area of rectangel

def rectangle(l, b):
    aor = l*b
    return f'The area of rectangle is: {aor}'

l = int(input('Enter the length of rectangle:'))
b = int(input('Enter the width of rectangle:'))
print(rectangle(l, b))