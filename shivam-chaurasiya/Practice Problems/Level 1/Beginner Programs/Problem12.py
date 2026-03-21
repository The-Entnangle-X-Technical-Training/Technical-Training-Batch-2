# Area of triangle

def triangle(b, h):
    aot = 1/2*b*h
    return f'The area of circle is: {aot}'

b = int(input('Enter the base of triangle:'))
h = int(input('Enter the height of triangle:'))
print(triangle(b, h))