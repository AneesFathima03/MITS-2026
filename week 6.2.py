RATE = 0.015 #1.5%
def calculate(oldbalance, charges, credit):
    '''calculate the new balance and minimum payment'''
    newbalance = (oldbalance * RATE) + charges - credit + oldbalance
    if newbalance <= 20:
        payment = newbalance
    else:
        payment = 20 + ((newbalance-20) * 0.10)
    return newbalance, payment
    

def display(newbalance, payment):
    ''' display the output'''
    print("New Balance = ${0: .2f}\nMinimum Payment = ${1:.2f}".format(newbalance, payment))
    
def getinput():
    ''' get the old balance, charges,credit'''
    oldbalance = float(input(" Enter old balance: "))
    charges = float(input(" Enter charges for the month: "))
    credit = float(input(" Enter credit: "))
    return oldbalance, charges, credit
def main():
    #input ---> process ---> output
    oldbalance, charges, credit = getinput()
    newbalance, payment = calculate(oldbalance, charges, credit)
    display(newbalance, payment)

main()
