def ceil(num):
    '''round non-integer up to next integer'''
    if int(num) != num:
        return int(num) + 1
    else:
        return int(num)


def semesterGrade(midterm, final):
    '''calculate semester grade'''
    average = (midterm + 2 * final) / 3
    average = ceil(average)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return average, grade


def display(average, grade):
    '''display output'''
    print("Semester average:", average)
    print("Semester grade:", grade)


def getinput():
    '''get midterm and final marks'''
    midterm = float(input("Enter midterm grade: "))
    final = float(input("Enter final exam grade: "))
    return midterm, final


def main():
    midterm, final = getinput()
    average, grade = semesterGrade(midterm, final)
    display(average, grade)


main()
