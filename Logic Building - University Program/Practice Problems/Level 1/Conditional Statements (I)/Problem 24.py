temperature = int(input("Enter the temperature (in celsius): "))

if temperature < 15:
    print("The temperature is cold.")
elif temperature >= 15 and temperature <= 30:
    print("The temperature is normal.")
elif temperature > 30:
    print("The temperature is hot.")
else:
    print("Invalid.")
    