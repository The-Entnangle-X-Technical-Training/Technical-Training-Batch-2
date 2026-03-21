# Days to Years, Weeks, Days Converter

total_days = int(input('Enter the total number of days: ')) # 380

year = 365
years = total_days // 365             # 1

rem_after_years = total_days % 365    # 15

weeks = rem_after_years//7          # 1

rem_days = rem_after_years%7        # 1

print(f'Total number of days: {total_days}')
print(f'Years: {years}')
print(f'weeks: {weeks}')
print(f'Remaining days: {rem_days}')