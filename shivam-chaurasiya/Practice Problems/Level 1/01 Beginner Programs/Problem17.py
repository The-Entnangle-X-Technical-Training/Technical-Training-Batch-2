# Seconds to Hours:Minutes:Seconds Converter

total_seconds = int(input('Enter the total number of seconds:'))  # 3700 seconds

# Hours Calculate
hours = total_seconds//3600             # 1 hour

# Remaining seconds after taking out hours
rem_after_hours = total_seconds%3600    # 100 seconds

# Minutes from remaining seconds
minutes = rem_after_hours//60           # 1 minute

# Final Remaining seconds 
remaining_seconds = rem_after_hours%60  # 40 seconds

print(f'Total Seconds: {total_seconds}')
print(f'Hours:Minuts:Seconds:{hours:02d}:{minutes:02d}:{remaining_seconds:02d}')