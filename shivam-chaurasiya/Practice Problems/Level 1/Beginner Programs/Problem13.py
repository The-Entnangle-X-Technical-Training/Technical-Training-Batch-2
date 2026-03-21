# Area and Perimeter of square

def square(s):
    aos = s*s
    pos = 4*s
    return f'The area of square is: {aos} and The Perimeter of square is: {pos}'

s = int(input('Enter the side of square:'))
print(square(s))