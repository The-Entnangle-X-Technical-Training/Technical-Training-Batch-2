# Arithmetic Progression - Print Series
# Write a program that takes first term (a), common difference (d), and N, then prints first N terms of AP.
# a (First Term): Series jahan se shuru ho rahi hai.
# d (Common Difference): Har step par kitna jodna (add karna) hai.
# N (Number of terms): Aapko kitne numbers tak series chahiye.


a = int(input('Enter a first term (a): '))          # 5
d = int(input('Enter a common difference (d): '))   # 3
n = int(input('Enter a number of terms (N): '))     # 4
    
for _ in range(n):
    print(a, end=' ')
    a = a + d
    
# count = 0
# while count < n:
#     print(a, end=' ')
#     a = a + d
#     count+=1
    