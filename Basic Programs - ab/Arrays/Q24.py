#Problem 24: Display Elements at Odd Positions 
#Write a program that displays elements at odd indices (1, 3, 5, ...).
arr=[13,5,7,8,9,6,4,3,2,-1,-67]
for i in range(1,len(arr),2):
    print(f'Array at {i} index: ',arr[i])