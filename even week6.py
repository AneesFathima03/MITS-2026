def is_even(n):
    '''return True if n is even'''
    return n % 2 == 0


def display(result, n):
    '''display output'''
    print("Number:", n)
    print("Is even:", result)


def main():
    n = int(input("Enter a number: "))
    result = is_even(n)
    display(result, n)


main()
