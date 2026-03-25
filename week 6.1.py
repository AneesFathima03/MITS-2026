def cost(ounces):
    ''' function to calculate cost of the post by weight 5 cents forthe first ounce and 10 centsand 10 cents for each additional ounce '''
    return 0.05 + 0.1 * ceil(ounces-1)
    

def ceil(num):
    ''' round non-integer number up to the next integer'''
    if int(num) != num:
        return int(num+1)
    else:
        return num

def getInput():
    '''get the wait of the post in ounce by the user'''
    return float(input("Enter the numbrer of ounces: "))
    

def main():
    ounces = getInput()
    postageCost = cost(ounces)
    print("Cost = ${0:.2f}".format(postageCost))
main()
