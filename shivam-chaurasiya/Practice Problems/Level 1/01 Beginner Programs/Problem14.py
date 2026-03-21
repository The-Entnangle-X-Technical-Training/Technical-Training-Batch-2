# Area and Perimeter of Rectangle

# Area of rectangle = l × b 
# Perimeter of rectangle = 2(l + b)

def rectangle(l, b):
    aor = l*b
    por = 2*(l*b)
    return f'The area of rectangle is: {aor} and The Perimeter of rectangle is: {por}'

l = int(input('Enter the length of rectangle:'))
b = int(input('Enter the width of rectangle:'))
print(rectangle(l, b))