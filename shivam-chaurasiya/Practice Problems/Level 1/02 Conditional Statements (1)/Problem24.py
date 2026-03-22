# Temperature Check
# Write a program that takes temperature as input and displays:
# "Cold" if temperature < 15
# "Normal" if temperature is 15-30
# "Hot" if temperature > 30

temperature = int(input('Enter the temperature: '))

if temperature < 15:
    print("Cold")
elif temperature <= 30:
    print("Normal")
else:
    print("Hot")
    