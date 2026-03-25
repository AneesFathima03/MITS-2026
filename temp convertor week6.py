def fahrenheit_to_celsius(f):
    '''convert fahrenheit to celsius'''
    return (f - 32) * 5/9


def display(celsius, f):
    '''display output'''
    print("Fahrenheit:", f)
    print("Celsius:", round(celsius, 2))


def main():
    f = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(f)
    display(celsius, f)


main()
