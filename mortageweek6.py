def getinput():
    '''get annual interest rate, monthly payment, and beginning balance'''
    annual_rate = float(input("Enter annual rate of interest: "))
    monthly_payment = float(input("Enter monthly payment: "))
    beginning_balance = float(input("Enter beg. of month balance: "))
    return annual_rate, monthly_payment, beginning_balance


def calculate(annual_rate, monthly_payment, beginning_balance):
    '''calculate interest paid, reduction of principal, and end balance'''
    monthly_rate = annual_rate / 100 / 12
    interest_paid = beginning_balance * monthly_rate
    reduction_principal = monthly_payment - interest_paid
    end_balance = beginning_balance - reduction_principal
    return interest_paid, reduction_principal, end_balance


def display(interest_paid, reduction_principal, end_balance):
    '''display the output'''
    print("Interest paid for the month: ${0:,.2f}".format(interest_paid))
    print("Reduction of principal: ${0:,.2f}".format(reduction_principal))
    print("End of month balance: ${0:,.2f}".format(end_balance))


def main():
    annual_rate, monthly_payment, beginning_balance = getinput()
    interest_paid, reduction_principal, end_balance = calculate(
        annual_rate, monthly_payment, beginning_balance
    )
    display(interest_paid, reduction_principal, end_balance)


main()
