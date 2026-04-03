#Problem 23: Display Elements at Even Positions 
#Write a program that displays elements at even indices (0, 2, 4, ...)
arr=[13,5,7,8,9,6,4,3,2,-1,-67]
for i in range(0,len(arr),2):
    print(f'Array at {i} index: ',arr[i])