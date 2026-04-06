# Pyramid - Single Star Growth
# Write a program that prints centered pyramid with stars for N rows.
#     *
#    * *
#   * * *
#  * * * *

n = int(input('Enter a rows: '))
    
for i in range(1, n + 1):
    print("-" * (n - i) + "*-" * i)
