seconds=int(input("Enter the number of seconds you want to convert: "))
hours=seconds//3600
minutes=int((seconds%3600)/60)
rem_seconds=((seconds%3600))%60
print(hours)
print(minutes)
print(rem_seconds)