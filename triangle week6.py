def triangle_area(b, h=1):
    '''calculate area of triangle with default height = 1'''
    return 0.5 * b * h


def display(area, b, h):
    '''display output'''
    print("Base:", b)
    print("Height:", h)
    print("Area:", area)


def main():
    b = float(input("Enter base: "))
    h = float(input("Enter height (press Enter for default 1): ") or 1)
    
    area = triangle_area(b, h)
    display(area, b, h)


main()
