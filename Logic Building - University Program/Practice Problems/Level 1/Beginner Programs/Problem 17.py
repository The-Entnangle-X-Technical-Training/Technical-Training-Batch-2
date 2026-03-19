#Problem 17: Seconds to Hours:Minutes:Seconds Converter

Total_seconds = int(input("Enter the seconds: "))

Hours = int(Total_seconds//3600)
Seconds_Remaining = int(Total_seconds % 3600)
Minutes = int(Seconds_Remaining//60)
Seconds = int(Seconds_Remaining % 60)

print(f" {Hours:02d}:{Minutes:02d}:{Seconds:02d}")