def convert_to_fahrenheit(celsius: int) -> int:
    fahrenheit = (1.8 * int(celsius)) + 32
    return round(fahrenheit)

def convert_to_celsius(fahrenheit: int) -> int:
    celsius = (fahrenheit - 32) * (5 / 9)
    return round(celsius)


celsius = input("Enter the Temperature in Celsius :")
print("Temperature in Fahrenheit :", convert_to_fahrenheit(celsius))