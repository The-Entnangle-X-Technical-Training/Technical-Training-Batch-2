# Simple Diagonal Pattern
# Write a program that prints stars diagonally for N rows.
# *
#  *
#   *
#    *

n = int(input('Enter a rows: '))    # 4

for i in range(n):
    print(" " * i + "*")
