def factorial(n):
    '''calculate factorial of n'''
    result = 1
    for i in range(1, n):
        result *= i
    return result


def isPrime(n):
    '''check prime using Wilson’s Theorem'''
    if n <= 1:
        return False
    return (factorial(n) + 1) % n == 0


def display(result, n):
    '''display output'''
    if result:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")


def getinput():
    '''get number from user'''
    return int(input("Enter a number: "))


def main():
    n = getinput()
    result = isPrime(n)
    display(result, n)


main()
