total_sec = int(input("Enter total number of second :"))

# i solved this math by myself :)

hr = total_sec/3600
minute = (total_sec%3600)/60
sec = (total_sec%3600)%60


print(f"{int(hr)} : {int(minute)} : {int(sec)}")