# 1. LENGTH CONVERTER

def length_converter():

    print("\n--- LENGTH CONVERSION ---")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Centimeters to Meters")
    print("4. Meters to Centimeters")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(value, "km =", value * 1000, "meters")

    elif choice == 2:
        print(value, "meters =", value / 1000, "km")

    elif choice == 3:
        print(value, "cm =", value / 100, "meters")

    elif choice == 4:
        print(value, "meters =", value * 100, "cm")

    else:
        print("Invalid choice!")


# 2. TEMPERATURE CONVERTER

def temperature_converter():

    print("\n--- TEMPERATURE CONVERSION ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter temperature: "))

    if choice == 1:
        fahrenheit = (value * 9 / 5) + 32
        print(value, "°C =", fahrenheit, "°F")

    elif choice == 2:
        celsius = (value - 32) * 5 / 9
        print(value, "°F =", celsius, "°C")

    else:
        print("Invalid choice!")


# 3. WEIGHT CONVERTER

def weight_converter():

    print("\n--- WEIGHT CONVERSION ---")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter weight: "))

    if choice == 1:
        print(value, "kg =", value * 1000, "grams")

    elif choice == 2:
        print(value, "grams =", value / 1000, "kg")

    else:
        print("Invalid choice!")


# 4. MAIN MENU

while True:

    print("       UNIT CONVERTER")
    print("1. Length Conversion")
    print("2. Temperature Conversion")
    print("3. Weight Conversion")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        length_converter()

    elif choice == 2:
        temperature_converter()

    elif choice == 3:
        weight_converter()

    elif choice == 4:
        print("Thank you for using Unit Converter!")
        break

    else:
        print("Invalid choice! Please try again.")